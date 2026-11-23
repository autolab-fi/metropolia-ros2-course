"""Stationary Octoliner demo. Identical ROS code in simulation and laboratory."""
import time
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import UInt16MultiArray


class SensorMonitor(Node):
    def __init__(self):
        super().__init__('sensor_monitor')
        self.velocity = self.create_publisher(Twist, 'robot/cmd_vel', 10)
        self.create_subscription(UInt16MultiArray, 'robot/line_sensors', self.observe, 10)
        self.create_timer(0.1, self.keep_stopped)
        self.last_log = 0.0
        self.get_logger().info('Waiting for eight line sensor channels; keeping velocity zero.')

    def keep_stopped(self):
        # In the laboratory, the first zero command arms the bounded controller.
        # Repeating zero keeps telemetry running without moving the wheels.
        self.velocity.publish(Twist())

    def observe(self, message):
        raw = list(message.data)
        if time.monotonic() - self.last_log >= 0.5:
            self.last_log = time.monotonic()
            self.get_logger().info(f'Right -> left ADC channels: {raw}')


def main():
    rclpy.init()
    node = SensorMonitor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            node.velocity.publish(Twist())
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
