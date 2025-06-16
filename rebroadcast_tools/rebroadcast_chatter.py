#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ReBroadcastChatter(Node):
    def __init__(self):
        super().__init__('rebroadcaster_chatter')
        self.sub = self.create_subscription(String, '/chatter', self.cb, 10)
        self.pub = self.create_publisher(String, '/chatter_local', 10)

    def cb(self, msg):
        self.get_logger().info(f'[rebroadcast] {msg.data}')
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = ReBroadcastChatter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
