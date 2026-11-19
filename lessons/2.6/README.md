# 2.6 Reach a target point

In this integration lesson, you will use position feedback to move a robot to a target and stop. The starting code is complete so that you can first inspect a working example. Earlier lessons will build each part step by step.

## Your goal

Start near **(0.40 m, -0.185 m)** facing along the positive x axis. Reach **(0.60 m, -0.185 m)**, then publish zero velocity and remain stopped for at least half a second. The checker accepts a position within **0.03 m** of the target. Coordinates are measured from the arena's origin, not from where the robot starts.

## Before you run

ROS2 connects independent programs called **nodes** using named **topics**. This program is one node. The platform provides the robot's position; your node decides what velocity to request.

- `robot/pose` carries `geometry_msgs/msg/PoseStamped`: position in metres, orientation as a quaternion, and a timestamp. In this first pilot the position describes the camera tag centre. It is not wheel odometry.
- `robot/cmd_vel` carries `geometry_msgs/msg/Twist`. Set `linear.x` for forward speed in metres per second and `angular.z` for turning speed in radians per second. Other fields are unused.

The bridge converts the existing camera map into a right-handed ROS frame: x increases to the right, y increases upward, and positive yaw is counterclockwise. The tag centre is below the origin, so its y coordinate is negative. The physical motion bridge uses these same signs; learner code is identical in both environments.

## Step 1: inspect the imports

`rclpy` is the normal ROS2 Python library. `Node` provides publishers, subscriptions and timers. `PoseStamped` and `Twist` are message classes. No robot-specific student library is required.

## Step 2: find the publisher and subscription

`create_publisher(Twist, 'robot/cmd_vel', 10)` creates a publisher. The last argument is a queue depth: keep up to ten messages while delivery catches up.

`create_subscription(PoseStamped, 'robot/pose', self.observe, 10)` calls `observe` whenever a new pose arrives. This callback is the control loop. There is no need to repeatedly ask the camera for an image.

## Step 3: calculate the direction

Subtract the current x and y from the target to obtain `dx` and `dy`. `math.atan2(dy, dx)` gives the direction toward the target. The quaternion stores orientation; for this flat arena, `2 * atan2(q.z, q.w)` recovers yaw. The wrapped angle difference avoids a sudden jump at -π / +π.

## Step 4: choose a safe velocity

The example turns in place when facing away from the target. Once facing the target, it drives at `0.04` m/s. The angular command is proportional to the heading error and limited to ±`0.8` rad/s. Forward velocity must stay between `0` and `0.05` m/s.

When the remaining distance is at most `0.025` m, the new `Twist()` stays zero. The node continues publishing that zero command on each pose callback. Keep sending commands: losing fresh commands stops the robot automatically.

## Step 5: check in the simulator

Choose **Start session** in Terminals. Your personal Linux environment starts on
the server with a live simulator. It does not reserve the real robot. All
terminals share `/workspace/ros2_ws` and its files.

The example is a normal ROS2 Python package. Open its node:

```bash
nano src/my_robot/my_robot/controller.py
```

Use the arrow keys to move through the code. In nano, **Ctrl+O**, then **Enter**
saves the file; **Ctrl+X** closes the editor. Save before running or submitting.

Run the practice check from your terminal:

```bash
check-in-sim
```

This resets the virtual robot, builds your package with `colcon build`, runs the
commands in `run.sh` and checks that the robot reaches the target and stops. Watch
the **Simulator** view. The feedback appears in the terminal. This practice run
does not create a graded laboratory result.

To build and run manually instead:

```bash
bash run.sh
```

The node keeps running until you press **Ctrl+C**. Open a second terminal with
**+** and inspect the real ROS graph:

```bash
ros2 node list
ros2 topic list
ros2 topic echo /robot/pose
```

`echo` continues printing incoming messages; **Ctrl+C** stops it. Each terminal is
a separate shell, so its current directory and sourced environments are local to
that shell. The base ROS2 environment is sourced automatically. After building, use
`source install/setup.bash` in any new terminal that needs your own package.

Use **+** to open another terminal and **×** beside a terminal tab to close it.
Closing a terminal stops its running processes, so save nano before closing.
Saved files remain in the shared workspace. You can close every terminal and
open a new one with **+**; **End session** ends the whole development environment.

ROS discovery can take a few seconds. If `ros2 node list` initially shows no
nodes, run it again, or use `ros2 node list --no-daemon --spin-time 2`.

Stop a manually running controller with Ctrl+C before `check-in-sim`, so two
controllers do not publish competing commands. You can also reset the model:

```bash
ros2 service call /simulation/reset std_srvs/srv/Empty '{}'
```

Change the forward speed from `0.04` to `0.02`, save and run `check-in-sim` again.
Does the arrival time change? Restore the original speed afterward.

## Step 6: check in the laboratory

Save all files and choose **Check in lab**. The platform freezes `src/` and
`run.sh`; later edits do not change that submission. Build/install/log directories
are temporary and are not submitted. The Raspberry Pi builds the saved package
for its own architecture.

The robot joins the same device queue as the Python and OpenCV courses. It first
leaves the dock if needed and moves to the starting pose using the existing reset
procedure. Your ROS2 process starts after positioning. Switch the robot view to
**Lab attempt** to see this attempt; **Simulator** still shows your personal model.

Queue and positioning time are separate from the maximum 60 seconds of active control. The checker observes the camera independently of your node. Publishing a pose or printing “passed” cannot pass the task. **Stop lab check** cancels this attempt and waits for the normal robot stop procedure.

Project build and launch have a separate limit of 45 seconds. No movement command
is sent while the package is being built.

Your development session lasts up to 30 minutes, with a 10-minute terminal idle
limit. Source files are backed up every 30 seconds and on End session; save and
end explicitly before leaving. A new session restores the last saved sources.
Unsaved nano buffers, generated files and running processes are not restored.

## Try and explain

1. Why do we stop inside a small region instead of requiring exact floating-point coordinates?
2. What happens if the node exits before reaching the target?
3. Why does the robot need fresh commands even when the requested speed is zero?
4. Which part of the code changes when you move the target?

Do not change the target for the graded check. Custom targets belong in a later exploration activity.
