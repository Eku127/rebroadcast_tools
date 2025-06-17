#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, CameraInfo

class ReBroadcastImageRaw(Node):
    def __init__(self):
        super().__init__('rebroadcaster_image_raw')

        # color image (uncompressed)
        self.color_sub = self.create_subscription(
            Image,
            '/camera/camera/color/image_raw',
            self.cb_color,
            10
        )
        self.color_pub = self.create_publisher(
            Image,
            '/rebroadcast/color/image_raw',
            10
        )

        # depth image (uncompressed)
        self.depth_sub = self.create_subscription(
            Image,
            '/camera/camera/aligned_depth_to_color/image_raw',
            self.cb_depth,
            10
        )
        self.depth_pub = self.create_publisher(
            Image,
            '/rebroadcast/aligned_depth_to_color/image_raw',
            10
        )

        # camera info
        self.caminfo_sub = self.create_subscription(
            CameraInfo,
            '/camera/camera/color/camera_info',
            self.cb_caminfo,
            10
        )
        self.caminfo_pub = self.create_publisher(
            CameraInfo,
            '/rebroadcast/color/camera_info',
            10
        )

    def cb_color(self, msg):
        self.color_pub.publish(msg)

    def cb_depth(self, msg):
        self.depth_pub.publish(msg)

    def cb_caminfo(self, msg):
        self.caminfo_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = ReBroadcastImageRaw()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
