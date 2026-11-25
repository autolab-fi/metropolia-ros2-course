# 1.3 Read a topic and understand its message

Your goal is to identify a topic's type and read one field from a real message.
A topic name alone does not explain the structure of the data it carries.

## Find topics and their types

Start this lesson's session. Run:

```bash
ros2 topic list -t
```

`topic list` lists discovered topics. The `-t` option also displays message types.
Look for the coordinate topic. Then inspect it:

```bash
ros2 topic info /robot/pose
```

You should see `geometry_msgs/msg/PoseStamped`, a publisher count and a subscription
count. A topic can have multiple subscribers. Inspector itself can contribute a
subscription; opening a viewer does not change the meaning of the message.

## Read the message definition

Run:

```bash
ros2 interface show geometry_msgs/msg/PoseStamped
```

A message **interface** defines named fields. `PoseStamped` combines a `header`
and a `pose`. The pose has a position and orientation. The header identifies the
reference frame and the time of the observation. Nested fields belong to their
parent object: `header.frame_id` means the `frame_id` inside `header`.

Now receive one actual message:

```bash
ros2 topic echo /robot/pose --once
```

`echo` displays messages. `--once` exits after one, returning you to the prompt.
Without `--once`, new messages keep arriving until you press **Ctrl+C**.

Look for output with this structure (timestamp numbers will differ):

```yaml
header:
  stamp:
    sec: ...
    nanosec: ...
  frame_id: map
pose:
  position:
    x: 0.4
    y: -0.185
    z: 0.0
```

Position is expressed in metres in the arena's map frame. Orientation is a
quaternion, not a single angle in degrees; we will interpret it in a later task.
Do not expect the timestamp or every coordinate to match a screenshot exactly.

## Compare the viewer and terminal

Open **ROS Inspector → Topics** and select `/robot/pose`. Find the same type and
`header.frame_id` field in the JSON preview. YAML in the terminal and JSON in the
viewer are two presentations of the structured ROS message.

You can also run:

```bash
ros2 topic hz /robot/pose
```

After a few seconds, it reports an observed rate near 10 messages per second in
this simulator. **Ctrl+C** stops the observer. This is a measured arrival rate;
it is not a promise that every program executes at exactly that rate.

## Save and check

Edit `nano src/answers.json` and replace each `TODO`:

| Key | Answer to find |
| --- | --- |
| `topic_name` | The full coordinate topic name |
| `message_type` | Its complete package/msg/type identifier |
| `frame_id` | The string inside `header.frame_id` |

Save with **Ctrl+O**, **Enter**, then leave with **Ctrl+X**. Choose **Check in
simulator** and read **Output**. If a criterion fails, revisit the corresponding
command and correct the saved answer. This lesson does not reserve a robot.
