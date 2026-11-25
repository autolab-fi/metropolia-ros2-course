# 1.5 Write a Python publisher

Your goal is to replace the CLI publisher with your own Python node. It must send
20.5 on `/learning/temperature` five times per second, using `Float32` messages.
This lesson does not send movement commands or reserve the physical robot.

## Open the starter

Start the session and open:

```bash
nano src/my_robot/my_robot/controller.py
```

The directories form a prepared Python ROS package. You do not need to construct
the package yet. `run.sh` launches this file directly for these first exercises.
The starter contains runnable structure and three TODO comments to complete.

## Understand the existing structure

`import rclpy` loads the ROS2 Python client library. `Node` is its node class;
`Float32` is the generated Python message class. A Python **class** groups data
and functions describing an object. `TemperaturePublisher(Node)` inherits ROS
node functionality. `self` refers to the current object.

`__init__` initializes a new object. The existing line:

```python
super().__init__('temperature_publisher')
```

initializes the ROS node with a name. A node name and a topic name identify
different things; the node will appear as `/temperature_publisher` in Inspector.

## Complete the publisher and timer

Inside `__init__`, replace the first TODO with:

```python
self.publisher = self.create_publisher(Float32, 'learning/temperature', 10)
```

The arguments specify the message type, topic name and history depth. Depth 10
means a bounded history of up to ten messages, not a publication frequency.
The relative name `learning/temperature` resolves to `/learning/temperature` in
this exercise's root namespace.

Replace the timer TODO with:

```python
self.timer = self.create_timer(0.2, self.publish_temperature)
```

The period is in seconds: `1 / 0.2 = 5` calls per second. The method
`publish_temperature` is a **callback**, a function ROS calls when the timer is
ready. We pass the method itself, without parentheses; adding `()` would call
it immediately instead of registering it for later calls.

Inside that callback, the starter creates `message = Float32()` and assigns
`message.data = 20.5`. Complete it with:

```python
self.publisher.publish(message)
```

Indent these lines consistently with the surrounding code. Python uses indentation
to group statements; a line in the wrong block can change the program or cause an
`IndentationError`. Save with **Ctrl+O**, **Enter**, then **Ctrl+X**.

## Run and inspect your node

Run `bash run.sh` in Terminal 1. The existing `main()` calls `rclpy.init()`, creates
your node, and calls `rclpy.spin(node)`. Spin processes timer and subscription
callbacks until interrupted; creating a timer without spinning is insufficient.
The `finally` block destroys the node and shuts down its ROS context on exit.

In Terminal 2, run:

```bash
ros2 node info /temperature_publisher
ros2 topic echo /learning/temperature
```

Stop the continuous echo with **Ctrl+C**. In **ROS Inspector → Nodes**, expand
`/temperature_publisher` and follow its publication to the message preview.
The observed rate should be near five messages per second.

## Check and investigate

Stop the manually launched node with **Ctrl+C** in Terminal 1. Choose **Check in
simulator**, then read **Output**. The check verifies the node name, topic/type
and repeated values. You can use `check-in-sim` for terminal practice first.

Try changing only the timer period to 0.5, run again and measure with
`ros2 topic hz /learning/temperature` in another terminal. It should be near
2 messages per second. Stop both programs and restore the original period.
The graded task checks repeated correct messages, not exact wall-clock timing.
If your node is absent, inspect Python errors in the launch terminal; if it is
present but silent, inspect the timer and publish call.
