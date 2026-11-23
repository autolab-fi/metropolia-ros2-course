# 1.1 ROS2 sandbox: observe, drive and run a node

Use this activity to explore the whole workflow before writing a node yourself.
The starting project is complete. First use normal ROS commands to move the
virtual robot, then run the Python node, and finally submit its files to the lab.

## 1. Start your personal environment

Choose **Start session** in **Terminals**. A Linux container and a simulator start
together on the server. The **Simulator** view shows the robot immediately;
you do not need to run a check first. Its live sample number advances even when
the robot is stationary. If updates stop, the view reports an interruption.

Use **+** to open more terminals, up to four. These are independent shells in
the same container, sharing `/workspace/ros2_ws` and its files. Use them as:

| Terminal | Suggested use |
| --- | --- |
| Terminal 1 | Edit the Python node with nano |
| Terminal 2 | Build and run the node, or publish a manual command |
| Terminal 3 | Observe incoming ROS messages |
| Terminal 4 | Inspect nodes or reset the simulator |

This environment does not reserve the real robot. Commands in these terminals
control only your simulator. The model provides pose feedback and velocity
commands; it does not yet simulate camera images, encoders or wheel slip.

## 2. Discover the ROS graph

A **node** is a running ROS program. A **topic** is a named channel carrying
messages of a particular type. In any terminal, run these commands one at a time:

```bash
ros2 node list
ros2 topic list
ros2 topic info /robot/pose
ros2 topic info /robot/cmd_vel
```

The platform node is `/ondroid_bridge`. It publishes
`/robot/pose` (`geometry_msgs/msg/PoseStamped`) and subscribes to
`/robot/cmd_vel` (`geometry_msgs/msg/Twist`). Discovery may take a few seconds;
repeat the command if a node has not appeared yet.

In Terminal 3, start a continuous observer:

```bash
ros2 topic echo /robot/pose
```

New messages keep arriving. `pose.position.x` and `y` are metres in the arena;
the initial position is approximately `(0.40, -0.185)`. Orientation is a
quaternion. The timestamp changes even when the position does not.
**Ctrl+C** stops this command. It does not end your environment.

Open **ROS Topics → Live workspace** to see the latest pose and, once you send
one, the latest velocity message. These are your interactive messages, separate
from **Saved attempt** observations. A displayed command is the last received
message, not proof that the robot is still moving.

## 3. Move without a Python node

In Terminal 2, publish a forward velocity ten times per second:

```bash
ros2 topic pub --rate 10 /robot/cmd_vel geometry_msgs/msg/Twist '{linear: {x: 0.03}, angular: {z: 0.0}}'
```

Watch the robot move in **Simulator** and the x coordinate change in Terminal 3
and ROS Topics. After about two seconds, press **Ctrl+C** in Terminal 2.
The command stream stops; the model stops within about half a second.
No check, recording or laboratory booking is needed for this experiment.

Try turning in place, then stop with **Ctrl+C**:

```bash
ros2 topic pub --rate 10 /robot/cmd_vel geometry_msgs/msg/Twist '{linear: {x: 0.0}, angular: {z: 0.4}}'
```

The accepted limits are forward speed `0`–`0.05` m/s and turning speed
`-0.8`–`0.8` rad/s. An out-of-range command stops the model.

## 4. Reset, edit and run the project

Stop every velocity publisher and controller with **Ctrl+C** first. In Terminal 4:

```bash
ros2 service call /simulation/reset std_srvs/srv/Empty '{}'
```

The robot returns to its starting pose and the displayed trail clears.
Reset does not kill your programs: a controller left running could move it again.

In Terminal 1, open the complete example:

```bash
nano src/my_robot/my_robot/controller.py
```

Find `create_subscription`: each pose message calls `observe`. That function
compares the current position with `(0.60, -0.185)` and publishes a velocity.
It publishes zero when close enough. `rclpy` is the standard ROS2 Python library;
there is no platform-specific student control library.

Save with **Ctrl+O**, then **Enter**; leave nano with **Ctrl+X**. In Terminal 2:

```bash
bash run.sh
```

This builds the package with `colcon`, sources the installed package and runs
its controller. Compilation may take a few seconds. The robot then moves toward
the target and stops; the node keeps publishing zero until you press **Ctrl+C**.
The simulator updates while this ordinary terminal command runs.

Change `command.linear.x = 0.04` to `0.02`, save, stop the old node, reset and
run again. Arrival should take longer. Editing a file does not automatically
restart a running Python process. Restore `0.04` for the final check.

Only one controller should publish velocity at a time. `ros2 topic info
/robot/cmd_vel` helps find competing publishers. Stop observers when you no
longer need their output.

## 5. Rehearse the fixed goal

Stop your manually started controller, then run:

```bash
check-in-sim
```

This resets, builds and runs the saved project. It checks that the robot reaches
`(0.60, -0.185)` within `0.03` m and publishes zero for at least half a second.
It stops its controller afterward and prints **Practice passed.** on success.
This is terminal practice feedback, not a graded course submission.

## 6. Check the same saved project in the laboratory

Save nano and choose **Check in lab**. This is the only action here that requests
the physical robot. It freezes `src/` and `run.sh`, queues the existing robot
workflow, positions the robot, rebuilds the package on the Raspberry Pi and runs
it for at most 60 seconds of active control. Queue, positioning and build time
are separate. The grading goal is the same as in step 5.

Temporary terminal commands, shell history and running processes are **not**
copied. The laboratory runs only the saved project. A manual turn performed in
step 3 does not make the physical robot turn. Later file edits do not change an
already submitted snapshot.

**Output** shows queue/reset events and the result. **Simulator / Lab → Lab
attempt** shows that attempt's measured trajectory, not your personal model.
**ROS Topics → Saved attempt** shows its observations. Your interactive
simulator remains separate and available. **Stop lab check** cancels the check.

## Keep your work

Files under `src/` and `run.sh` are backed up every 30 seconds, before a lab
check and on **End session**. A session lasts up to 30 minutes, or 10 minutes
without terminal input. Unsaved nano buffers and running processes are not
restored. `build/`, `install/` and `log/` are temporary.

Save before switching activities: choosing another lesson ends this environment
and stops its processes. This sandbox and lesson 2.6 retain separate saved files.
Closing a terminal with **×** also stops its processes; it leaves shared files
and the simulator available to the other terminals.
