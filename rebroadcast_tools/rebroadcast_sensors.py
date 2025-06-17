#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage, CameraInfo
from nav_msgs.msg import Odometry

class ReBroadcastImageCompressed(Node):
    def __init__(self):
        super().__init__('rebroadcaster_image_compressed')

        # color image
        self.color_sub = self.create_subscription(
            CompressedImage,
            '/camera/camera/color/image_raw/compressed',
            self.cb_color,
            10
        )
        self.color_pub = self.create_publisher(
            CompressedImage,
            '/rebroadcast/color/image_raw/compressed',
            10
        )

        # depth image
        self.depth_sub = self.create_subscription(
            CompressedImage,
            '/camera/camera/aligned_depth_to_color/image_raw/compressed',
            self.cb_depth,
            10
        )
        self.depth_pub = self.create_publisher(
            CompressedImage,
            '/rebroadcast/aligned_depth_to_color/image_raw/compressed',
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

        # Odometry
        self.odom_sub = self.create_subscription(
            Odometry,
            '/Odometry_for_host',
            self.cb_odom,
            10
        )
        self.odom_pub = self.create_publisher(
            Odometry,
            '/rebroadcast/Odometry',
            10
        )

    def cb_color(self, msg):
        self.color_pub.publish(msg)

    def cb_depth(self, msg):
        self.depth_pub.publish(msg)

    def cb_caminfo(self, msg):
        self.caminfo_pub.publish(msg)
    
    def cb_odom(self, msg):
        self.odom_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = ReBroadcastImageCompressed()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
