# 1.4 Follow the line with ROS2

This complete demonstration is for testing the ROS environment before writing
its pieces yourself. The same Python node runs in the personal Linux simulator
and in the physical laboratory. No MQTT credentials or robot-specific student
control library is needed.

## What this demonstration does

The node follows the line for **55 seconds**, then publishes zero velocity and logs that the demo has finished. It passes the first green square and continues along the track; it no longer stops at the nearby target point. The ROS node remains running after stopping; use Ctrl+C to end it.

Both `bash run.sh` and Check in lab use this duration. Queue, positioning and runtime startup are separate from the 60-second active laboratory limit. The checker requires sustained forward commands, fresh line readings, at least 0.45 m measured travel and at least 0.25 m displacement from the start. Simply waiting in place will not pass. Simulation and physical hardware can cover different distances in the same time.

## Start it from Linux

Use **+** beside the terminal tabs to open Terminal 2, 3 or 4. They share
the same files, ROS graph and simulator; each shell has its own processes and
environment variables. Keep only one movement controller running at a time.

1. Choose this activity, then **Start session** in Terminals. Save nano before
   changing activities: the previous environment is saved and ended.
2. In Terminal 1, open the complete program:

```bash
nano src/my_robot/my_robot/controller.py
```

Save with Ctrl+O, Enter; leave nano with Ctrl+X. In Terminal 2, build and run:

```bash
bash run.sh
```

These single-file demos launch Python directly in the installed ROS environment,
so no package build is needed for the first run. Watch Simulator and ROS Inspector.
`/robot/line_sensors` uses `std_msgs/msg/UInt16MultiArray`; `message.data` contains
exactly eight ADC readings, channel **0 on the right**, channel **7 on the left**.
The eight bars show the readings; green marks channels with line contrast.
A flat reading is not sufficient evidence that a line is visible.

In another terminal, try these commands one at a time:

```bash
ros2 node list
ros2 topic list
ros2 topic echo /robot/line_sensors --once
ros2 topic echo /robot/cmd_vel
ros2 topic echo /demo/distance
```

Ctrl+C stops a continuously printing observer. In the terminal running the node,
Ctrl+C stops that node; the platform stops movement when commands stop arriving.
Only one velocity controller should run at once.

## Repeat a simulated check

Stop your manually running node with Ctrl+C first, then use:

```bash
check-in-sim
```

This resets the model and runs this activity's saved project/checker. Its feedback
is practice, without reserving a real robot. To reset manually, stop controllers
first and run:

```bash
ros2 service call /simulation/reset std_srvs/srv/Empty '{}'
```

Source files belong to this activity and are saved independently of other demos.

In **ROS Inspector → Nodes**, find `/follow_line`. Inspect its subscriptions
and publications. Select `/robot/line_sensors` for the sensor display,
`/robot/cmd_vel` for steering commands, or `/demo/distance` for displacement.

## Run the same code on the physical robot

Save all source files, then choose **Check in lab**. The existing queue positions
the robot and starts the same frozen Python node on the Raspberry Pi. The first explicit zero-velocity heartbeat arms the bounded hardware
controller, allowing physical sensor telemetry while the motors remain stopped.
The ROS node does not access I2C or MQTT itself.

Open **Lab** for the real overhead camera stream. After the check, the same
player offers its recording, using the existing laboratory video controls.
The recording is associated with this submitted attempt; older recordings can
expire under the normal video quota.

**ROS Inspector** automatically selects the laboratory when you submit Check in lab.
It shows the physical `/robot/pose`, `/robot/cmd_vel`, `/robot/line_sensors` and
`/demo/distance` when published. Its **Laboratory** label distinguishes these
observations from the personal simulator. Selecting **Simulator** returns the
panel to personal simulation topics; selecting **Lab** returns to physical data.
After completion, the last laboratory observations retain their timestamps.
Opening a saved laboratory check selects its observations and recording.
**Output** shows preparation, node logs and the final result.

Do not edit code after submitting and expect the running check to change: the
lab executes the saved snapshot. **Stop lab check** cancels that execution. A
completed Lab view retains its last observation; it is not a continuing sensor
connection. Saved checks can be opened from **Checks**.

## What to inspect in the source

- Publishers, subscriptions and the 0.1-second timer use ordinary `rclpy`.
- `Twist.linear.x` is forward m/s; `Twist.angular.z` is CCW rad/s.
- The zero command is published while data is missing or stale.
- The `demo_seconds` ROS parameter defaults to 55 seconds. The timer starts on the first forward command, and the completion log explains the final stop. The laboratory independently checks duration, actual camera-measured movement and line readings.
- Simulation raw values and board geometry are illustrative. Physical ADC values
  need not numerically equal simulated values; inspect contrast across channels.

The program finds relative contrast and splits neighbouring active channels
into separate dark regions. It follows the region nearest the previous line
position, then calculates its weighted left/right error. This matters in the real
arena: a coloured-zone edge can create an extra dark region. Averaging both
regions together can steer the robot away from the actual track. A positive error means the line is on the robot's left, so
positive angular.z turns toward it. In simulation, try reducing the forward
speed to see how it affects tracking. The physical motors need enough power to
overcome friction: 0.03 m/s stalled during testing on this stand. Begin physical
experiments with the starter's 0.04 m/s and compare requested motion with measured
pose. Keep the platform limits of 0.05 m/s and ±0.8 rad/s; the starter caps turning
at ±0.6 rad/s. Do not continue blindly when the line disappears:
missing/flat readings or data older than 0.35 seconds produce a zero command.
The laboratory also stops independently if trusted sensor telemetry is stale.

## Optional package workflow

The normal ament Python package remains in the workspace. To practise the
standard package build/run flow instead, stop the current node and use:

```bash
colcon build --symlink-install
source install/setup.bash
ros2 run my_robot controller
```

The default run.sh deliberately starts the same controller.py directly for fast
demonstration feedback. A lab check runs the exact saved run.sh; changing how you
launch a node manually does not change that snapshot script.

## Existing saved projects

Starting a new session upgrades an exact, unmodified copy of the previous
reference program to the 55-second demo. Your edited programs are preserved.
Stop the old node and end/restart your session to load the update. If an edited
controller still contains the old nearby-target stop,
replace `src/my_robot/my_robot/controller.py` with the current complete
[reference program](https://github.com/autolab-fi/metropolia-ros2-course/blob/main/lessons/1.4/solution.py)
in nano, save, stop the old node, reset the simulator and run again.
