import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class TemperaturePublisher(Node):
    def __init__(self):
        super().__init__('temperature_publisher')
        # TODO: create self.publisher for learning/temperature
        # TODO: create a timer calling publish_temperature every 0.2 seconds

    def publish_temperature(self):
        message = Float32()
        message.data = 20.5
        # TODO: publish message

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
