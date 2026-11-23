"""Move using pose feedback and publish a normal ROS Float32 distance topic."""
import math
import time
import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException
from geometry_msgs.msg import PoseStamped, Twist
from std_msgs.msg import Float32


class DriveAndTopics(Node):
    def __init__(self):
        super().__init__('drive_and_topics')
        self.velocity = self.create_publisher(Twist, 'robot/cmd_vel', 10)
        self.distance = self.create_publisher(Float32, 'demo/distance', 10)
        self.create_subscription(PoseStamped, 'robot/pose', self.observe, 10)
        self.create_timer(0.1, self.update)
        self.pose = None
        self.pose_at = 0.0
        self.initial = None
        self.done = False

    def observe(self, message):
        p = message.pose
        self.pose = (p.position.x, p.position.y, 2 * math.atan2(p.orientation.z, p.orientation.w))
        self.pose_at = time.monotonic()
        if self.initial is None:
            self.initial = self.pose[:2]

    def update(self):
        command = Twist()  # Always publish zero while waiting for fresh data.
        if self.pose and time.monotonic() - self.pose_at < 0.4:
            x, y, yaw = self.pose
            distance = math.hypot(x - self.initial[0], y - self.initial[1])
            self.distance.publish(Float32(data=distance))
            dx, dy = 0.60 - x, -0.185 - y
            self.done = self.done or math.hypot(dx, dy) <= 0.025
            if not self.done:
                error = math.atan2(math.sin(math.atan2(dy, dx) - yaw), math.cos(math.atan2(dy, dx) - yaw))
                command.angular.z = max(-0.8, min(0.8, 2.0 * error))
                command.linear.x = 0.03 if abs(error) < 0.4 else 0.0
        self.velocity.publish(command)


def main():
    rclpy.init()
    node = DriveAndTopics()
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
