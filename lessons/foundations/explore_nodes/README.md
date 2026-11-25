# 1.2 Find and inspect a ROS2 node

Your goal is to find a running node and identify what it publishes and subscribes
to. You will use both the terminal and ROS Inspector to investigate the same graph.

## Find the node

Start this lesson's session and wait for the `student@ros2:` prompt. Run:

```bash
ros2 node list
```

`ros2` is the ROS2 command-line tool. `node` selects node-related commands, and
`list` asks for discovered node names. You should find `/ondroid_bridge`. The
platform starts this node so the simulator and ROS can exchange messages.
Other inspection tools may also create short-lived nodes, so the list is not
necessarily limited to one entry. Discovery can take a moment; repeat the command
if the node does not appear immediately.

Now run:

```bash
ros2 node info /ondroid_bridge
```

`info` asks about one named node. Read these two sections:

- **Publishers**: topics to which this node sends messages.
- **Subscribers**: topics from which this node receives messages.

Services and other sections can be left for a later lesson. Keep the terminal
output available while you answer the questions below. If a section is above the
visible area, scroll upward inside the terminal to review earlier lines.

## Connect names to behavior

Find the publication carrying the robot's coordinates. Its type is
`geometry_msgs/msg/PoseStamped`. Find the subscription carrying motion commands;
its type is `geometry_msgs/msg/Twist`.

A publisher/subscriber relationship is a communication direction, not a physical
wire. The platform publishes pose because controllers need feedback. It subscribes
to velocity because controllers send movement requests.

Open **ROS Inspector → Nodes**, expand `/ondroid_bridge`, and compare its
publications and subscriptions with the terminal output. Select a listed topic
to open its details in **Topics**. Inspector subscribes to messages to display
previews, so some subscriptions belong to inspection itself.

## Complete the saved answers

Run:

```bash
nano src/answers.json
```

Replace each `TODO` using the actual names you found:

| Key | What to enter |
| --- | --- |
| `node_name` | The full name of the platform bridge node |
| `publishes` | Its coordinate topic, of type `geometry_msgs/msg/PoseStamped` |
| `subscribes` | Its motion-command topic, of type `geometry_msgs/msg/Twist` |

Use the leading `/`, preserve capitalization and keep the JSON quotes. Save with
**Ctrl+O**, **Enter**, then leave with **Ctrl+X**. Choose **Check in simulator**
and read the individual criteria in **Output**. The check evaluates your saved
answers; it does not claim to record whether you typed a command.

## Investigate independently

Run `ros2 node info` again with an incorrect node name. Read the error and then
repeat with the correct name. A missing node can mean a name is wrong or a program
has not been started; it does not automatically mean ROS is broken.

Do not stop `/ondroid_bridge`: it supplies this environment's simulation. In later
lessons, you will launch and stop your own nodes and see the graph change.
