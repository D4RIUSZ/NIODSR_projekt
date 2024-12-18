#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleSimCircle(Node):
    def __init__(self):
        super().__init__('turtle_circle')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.publish_command)

    def publish_command(self):
        msg = Twist()
        msg.linear.x = 10.0  # Prędkość liniowa (m/s)
        msg.angular.z = 10.5  # Prędkość kątowa (rad/s)

        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: linear.x = {msg.linear.x}, angular.z = {msg.angular.z}')

def main(args=None):
    rclpy.init(args=args)
    node = TurtleSimCircle()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

