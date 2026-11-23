"""Follow Octoliner readings; use pose only to finish inside the bounded demo goal."""
import math
import time
import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
from geometry_msgs.msg import PoseStamped, Twist
from std_msgs.msg import UInt16MultiArray, Float32


class FollowLine(Node):
    def __init__(self):
        super().__init__('follow_line')
        self.velocity = self.create_publisher(Twist, 'robot/cmd_vel', 10)
        self.distance = self.create_publisher(Float32, 'demo/distance', 10)
        self.create_subscription(UInt16MultiArray, 'robot/line_sensors', self.sense, 10)
        self.create_subscription(PoseStamped, 'robot/pose', self.observe, 10)
        self.create_timer(0.1, self.update)
        self.error = None
        self.sensor_at = self.pose_at = 0.0
        self.pose = self.initial = None
        self.done = False

    def sense(self, message):
        raw = list(message.data)
        self.sensor_at = time.monotonic()
        self.error = None
        if len(raw) != 8:
            return
        lo, hi = min(raw), max(raw)
        if hi - lo < 80:  # Flat readings do not establish that a line is visible.
            return
        weights = [max(0.0, (v - lo) / (hi - lo) - 0.5) for v in raw]
        total = sum(weights)
        if total:
            # Channel 0 is RIGHT, channel 7 is LEFT: positive means turn left.
            self.error = sum(((i - 3.5) / 3.5) * w for i, w in enumerate(weights)) / total

    def observe(self, message):
        self.pose = (message.pose.position.x, message.pose.position.y)
        self.pose_at = time.monotonic()
        if self.initial is None:
            self.initial = self.pose

    def update(self):
        command = Twist()
        now = time.monotonic()
        fresh_pose = self.pose and now - self.pose_at < 0.4
        if fresh_pose:
            x, y = self.pose
            self.distance.publish(Float32(data=math.hypot(x-self.initial[0], y-self.initial[1])))
            self.done = self.done or math.hypot(x-0.60, y+0.155) <= 0.028
        if fresh_pose and not self.done and now-self.sensor_at < 0.35 and self.error is not None:
            command.linear.x = 0.025
            command.angular.z = max(-0.6, min(0.6, 0.6*self.error))
        # Missing line, stale sensors or a completed goal => explicit zero.
        self.velocity.publish(command)


def main():
    rclpy.init()
    node = FollowLine()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        if rclpy.ok():
            node.velocity.publish(Twist())
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
