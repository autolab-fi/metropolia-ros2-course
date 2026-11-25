import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Doubler(Node):
    def __init__(self):
        super().__init__('doubler')
        self.publisher = self.create_publisher(Int32, 'learning/output', 10)
        # TODO: subscribe to learning/input with callback self.on_number

    def on_number(self, message):
        response = Int32()
        # TODO: assign twice the received integer to response.data
        # TODO: publish response

def main():
    rclpy.init()
    node = Doubler()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
