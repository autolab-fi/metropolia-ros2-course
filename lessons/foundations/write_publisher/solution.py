import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class TemperaturePublisher(Node):
    def __init__(self):
        super().__init__('temperature_publisher')
        self.publisher = self.create_publisher(Float32, 'learning/temperature', 10)
        self.timer = self.create_timer(0.2, self.publish_temperature)

    def publish_temperature(self):
        message = Float32()
        message.data = 20.5
        self.publisher.publish(message)

def main():
    rclpy.init()
    node = TemperaturePublisher()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
