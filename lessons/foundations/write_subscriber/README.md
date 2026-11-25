# 1.6 Receive a message and publish a response

Your goal is to write a node that receives integers on `/learning/input`, doubles
each value and publishes an integer response on `/learning/output`. The node
must react to new messages rather than publish one fixed answer.

## Follow the data flow

There will be three roles: an input publisher, your `/doubler` node, and an
observer of its output. Your node is both a subscriber and a publisher:

```text
input publisher → /learning/input → /doubler → /learning/output → observer
```

Both topics use `std_msgs/msg/Int32`. `Int32` holds an integer, unlike the
floating-point `Float32` used for temperature. Matching names without matching
types are insufficient for communication.

## Complete the node

Start the session and open:

```bash
nano src/my_robot/my_robot/controller.py
```

The starter already creates the `/doubler` node and its output publisher. Replace
the subscription TODO in `__init__` with:

```python
self.subscription = self.create_subscription(
    Int32, 'learning/input', self.on_number, 10
)
```

The arguments identify the input type, topic, callback and history depth.
`on_number` will receive the message object when a new input arrives. Keeping
the subscription on `self` also makes its role in this node explicit.

Inside `on_number`, a new output message is already constructed. Complete the
remaining TODOs:

```python
response.data = message.data * 2
self.publisher.publish(response)
```

`message.data` is the received integer. `response.data` is the integer you will
send. These are different message objects: receiving an input does not
automatically send an output. Save and leave nano.

## Test the whole exchange manually

1. In Terminal 1, run `bash run.sh`. Leave it running.
2. Open Terminal 2 with **+**, and run:

   ```bash
   ros2 topic echo /learning/output
   ```

   It waits: your node has not received any input yet. A waiting subscriber is
   not necessarily broken.
3. Open Terminal 3 and send one input:

   ```bash
   ros2 topic pub --once /learning/input std_msgs/msg/Int32 '{data: 7}'
   ```

   `--once` sends one message and exits. Terminal 2 should show `data: 14`.
4. Send 11 instead of 7. The next output should be 22.
5. Inspect `/doubler` in **ROS Inspector → Nodes**. Find both its subscription and
   publication; follow `/learning/output` to its latest message. The same graph
   can also be inspected with `ros2 node info /doubler`.
6. Stop the echo and your node with **Ctrl+C** in their respective terminals.

If the one-shot CLI publisher waits for a subscription, check that your node is
running and its subscription has the correct name and type. If output is always
zero, check which value you assign to `response.data`.

## Check behavior, not a memorized answer

Choose **Check in simulator**. The check launches your saved project and sends
several different, randomly chosen inputs. It requires the expected node,
input/output connections and at least three correctly doubled values. Printing
answers to the terminal or publishing a constant does not satisfy these criteria.
Read every criterion in **Output**, correct the saved file and try again.
`check-in-sim` provides the same criteria for terminal practice; stop manual
nodes before using it.

Your node currently runs in the personal simulator environment, but the exercise
only exchanges messages; it does not move the robot. In the following module,
you will apply these same publisher/subscriber patterns to real sensor feedback
and bounded physical robot checks.
