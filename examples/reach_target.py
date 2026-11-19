"""Reference solution for lesson 2.6. Distances are metres; angles are radians."""
import math

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped, Twist


class ReachTarget(Node):
    def __init__(self):
        super().__init__('reach_target')
        self.velocity = self.create_publisher(Twist, 'robot/cmd_vel', 10)
        self.create_subscription(PoseStamped, 'robot/pose', self.observe, 10)
        self.get_logger().info('Waiting for robot/pose')

    def observe(self, message):
        pose = message.pose
        target_x, target_y = 0.60, -0.185
        dx, dy = target_x - pose.position.x, target_y - pose.position.y
        q = pose.orientation
        yaw = 2 * math.atan2(q.z, q.w)
        error = math.atan2(math.sin(math.atan2(dy, dx) - yaw),
                           math.cos(math.atan2(dy, dx) - yaw))
        command = Twist()
        if math.hypot(dx, dy) > 0.025:
            command.angular.z = max(-0.8, min(0.8, 2.0 * error))
            command.linear.x = 0.04 if abs(error) < 0.4 else 0.0
        self.velocity.publish(command)


def main():
    rclpy.init()
    node = ReachTarget()
    try:
        rclpy.spin(node)
    finally:
        node.velocity.publish(Twist())
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
