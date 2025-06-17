#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

class ReBroadcastOdom(Node):
    def __init__(self):
        super().__init__('rebroadcaster_odom')

        # Odometry
        self.odom_sub = self.create_subscription(
            Odometry,
            '/Odometry',
            self.cb_odom,
            10
        )
        self.odom_pub = self.create_publisher(
            Odometry,
            '/Odometry_for_host',
            10
        )
    def cb_odom(self, msg):
        self.odom_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = ReBroadcastOdom()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
