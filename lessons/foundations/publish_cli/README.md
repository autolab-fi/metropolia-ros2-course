# 1.4 Publish your first ROS2 message

Your goal is to create a topic and send typed messages without writing Python.
We will publish a temperature value; this topic does not move the robot.

## Start a publisher

Start the session. In Terminal 1, run:

```bash
ros2 topic pub --rate 5 /learning/temperature std_msgs/msg/Float32 '{data: 20.5}'
```

Read the command in parts:

- `ros2 topic pub` starts a command-line publisher node.
- `--rate 5` asks it to publish five messages per second.
- `/learning/temperature` is our topic name. ROS discovers it when the publisher starts.
- `std_msgs/msg/Float32` is a message type containing one floating-point field, `data`.
- `'{data: 20.5}'` supplies that field using YAML. The single quotes keep the shell
  from treating the spaces and punctuation as separate arguments.

This command keeps running; the prompt does not return until you stop it. Use
**+** beside the terminal tabs to open Terminal 2. Both terminals use the same
ROS environment. In Terminal 2 run:

```bash
ros2 topic echo /learning/temperature
```

You should repeatedly see `data: 20.5`. Stop this observer with **Ctrl+C**.
The publisher in Terminal 1 continues running independently.

Open **ROS Inspector → Topics**, select `/learning/temperature`, and compare its
value with the terminal. In **Nodes**, find the CLI publisher; its generated name
usually starts with `/_ros2cli_`. It is a real node even though you did not write a
Python file. Stop the publisher with **Ctrl+C** in Terminal 1.

## Make the launch command part of the project

A saved check starts a fresh environment. It does not copy the command that was
running in your terminal. Save the command in the project's launch file:

```bash
nano run.sh
```

Keep the first two lines. Replace the comment and the `printf` line with:

```bash
exec ros2 topic pub --rate 5 /learning/temperature std_msgs/msg/Float32 '{data: 20.5}'
```

`source /opt/ros/jazzy/setup.bash` prepares the ROS commands in the shell.
`exec` replaces that shell with the publisher process, so stopping the launch
also stops its main program. `run.sh` is a shell script; `bash run.sh` executes
its saved commands. Save with **Ctrl+O**, **Enter**, then **Ctrl+X**.

Run `bash run.sh` manually and repeat the observation in Terminal 2. When finished,
stop both the observer and publisher with **Ctrl+C** in their own terminals.

## Check the saved project

Choose **Check in simulator**. Open **Output**: the check must discover a publisher,
verify the Float32 topic and receive at least three messages containing 20.5.
A printed success message or one message is insufficient. The check runs saved
`run.sh` in a separate environment, so your personal simulator remains available.

You can also type `check-in-sim` for local practice feedback in the terminal.
Stop manual nodes first: this helper launches the saved program too. The button
records a graded attempt; terminal practice does not award course credit.

## Experiment and diagnose

Change 20.5 to 21.0 in `run.sh`, save, run, and observe the different value.
A graded check should now explain that the required value was not received.
Restore 20.5 for the exercise. If no messages appear, check the spelling of the
topic, the message type, quotes and whether your publisher is still running.
