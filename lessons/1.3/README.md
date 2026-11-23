# 1.3 Move and publish a distance topic

This complete demonstration is for testing the ROS environment before writing
its pieces yourself. The same Python node runs in the personal Linux simulator
and in the physical laboratory. No MQTT credentials or robot-specific student
control library is needed.

## What this demonstration does

The node subscribes to pose, drives toward `(0.60, -0.185)` m, stops within 0.03 m, and publishes its displacement on `/demo/distance`. The controller continues publishing zero after arrival.

## Start it from Linux

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
so no package build is needed for the first run. Watch Simulator and ROS Topics.
`/robot/line_sensors` uses `std_msgs/msg/UInt16MultiArray`; `message.data` contains
exactly eight ADC readings, channel **0 on the right**, channel **7 on the left**.
The eight bars show the readings; green marks channels with line contrast.
A flat reading is not sufficient evidence that a line is visible.

In another terminal, try these commands one at a time:

```bash
ros2 node list
ros2 topic list
ros2 topic echo /demo/distance
ros2 topic echo /robot/cmd_vel
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

## Run the same code on the physical robot

Save all source files, then choose **Check in lab**. The existing queue positions
the robot and starts the same frozen Python node on the Raspberry Pi. The first explicit zero-velocity heartbeat arms the bounded hardware
controller, allowing physical sensor telemetry while the motors remain stopped.
The ROS node does not access I2C or MQTT itself.

Open **Lab** for the measured physical trajectory and its eight sensor readings.
The bars below this view are from the actual Octoliner, not an estimate from the
camera or simulator. **Output** shows preparation, node logs and the final result.
**ROS Topics** remains your personal simulator's data; it does not switch to lab
history. Queue/reset/build time precedes the bounded active-control phase.

Do not edit code after submitting and expect the running check to change: the
lab executes the saved snapshot. **Stop lab check** cancels that execution. A
completed Lab view retains its last observation; it is not a continuing sensor
connection. Saved checks can be opened from **Checks**.

## What to inspect in the source

- Publishers, subscriptions and the 0.1-second timer use ordinary `rclpy`.
- `Twist.linear.x` is forward m/s; `Twist.angular.z` is CCW rad/s.
- The zero command is published while data is missing or stale.
- Simulation raw values and board geometry are illustrative. Physical ADC values
  need not numerically equal simulated values; inspect contrast across channels.

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
