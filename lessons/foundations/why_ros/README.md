# 1.1 Why robots use ROS2

By the end of this lesson, you will explain **node**, **topic** and **message**,
and open the environment you will use throughout the course. No ROS experience
or Python program is required for this lesson.

## A robot has several jobs

Imagine a mobile robot following a line. One program reads a sensor. Another
calculates a steering correction. A third sends movement commands. We want to
inspect and replace one part without rewriting every other part.

ROS2 provides communication libraries, message types and development tools for
these programs. Despite the name Robot Operating System, ROS2 does not replace
Linux: our ROS2 programs run on Linux.

A **node** is a running participant in this system. A Python file sitting on disk
is source code; after you launch the program, it can create a ROS node.
One process can contain several nodes; our first programs each create one learner
node. A **topic** is a named message channel. A **publisher** sends messages to a topic;
a **subscriber** receives them. Every topic uses a message type describing the
fields and their kinds of values. A topic is not a saved file or a queue of tasks
waiting for the physical laboratory.

For example, our platform node publishes coordinates on `/robot/pose`. Your future
controller will subscribe to those coordinates and publish velocity commands on
`/robot/cmd_vel`. Another node can observe the same coordinates at the same time.
The names start with `/` because they are full names in the ROS graph: the set
of running nodes and their communication links.

## Open your personal environment

1. In **Terminals**, select **Start session**. Wait for the prompt containing
   `student@ros2:`. A prompt means the shell is ready for a command.
2. **Simulator** displays your virtual robot. The robot stays stopped unless a
   program publishes movement commands. This personal environment does not reserve
   the physical robot. No installation on your computer is needed.
3. Type the following command and press **Enter**:

   ```bash
   pwd
   ```

   You should see `/workspace/ros2_ws`. `pwd` prints the current directory.
4. Run `ls`. It lists the files and directories here. `src/` contains your source
   files; `run.sh` contains the command for launching the project.
5. Open **ROS Inspector → Nodes**. You should find `/ondroid_bridge`, the platform
   node connecting ROS messages to this personal simulator.
6. Open **Topics** and select `/robot/pose`. Its changing timestamp shows new
   messages arrive even while the virtual robot is stationary.

A terminal is a window into a Linux shell. Additional terminal tabs share the same
files and ROS system. They are useful for leaving one program running while you
inspect it from another terminal.

## Save your answers

Open the prepared file:

```bash
nano src/answers.json
```

`nano` is a terminal text editor. Use arrow keys to move the cursor and replace the
three `TODO` values. Choose one value from each row below:

| Key | Choices |
| --- | --- |
| `ros_role` | `communication_and_tools`, `linux_replacement`, `video_file` |
| `node` | `running_ros_component`, `directory`, `physical_wheel` |
| `topic` | `named_message_channel`, `python_file`, `laboratory_booking` |

Keep the double quotes and commas: this file is a **JSON object**, with a name
on the left of each colon and a value on the right. Do not add a comma after the
last entry. Use **Ctrl+O**, then **Enter**, to save; use **Ctrl+X** to leave nano.
Here `Ctrl` means holding the Control key while pressing the letter.

Choose **Check in simulator**. The check reads the saved answers, not your terminal
history. Open **Output** to see each PASS or FAIL with its explanation. **Checks**
keeps the attempts so you can reopen their results. Correct an answer, save and
check again if necessary. This lesson does not use the physical laboratory.

Files are saved separately for each lesson. Save before leaving a lesson; unsaved
nano text is not included in checks. **End session** stops your processes and keeps
saved source files for your next session.
