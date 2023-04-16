#!/usr/bin/python3

import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

# Set the image path
IMAGE_PATH = "/home/vortex/perception_ws/src/yolov5_wrapper/data/images.jpeg"


def main():
    # Initialize the ROS node
    rospy.init_node("image_publisher")

    # Create the image publisher
    image_pub = rospy.Publisher("/zed/rgb/image_rect_color", Image, queue_size=10)

    # Set the publishing rate (in Hz)
    rate = rospy.Rate(10)

    # Create a CvBridge object
    bridge = CvBridge()

    while not rospy.is_shutdown():
        # Load the image
        image = cv2.imread(IMAGE_PATH)

        # Convert the image to a ROS message
        image_msg = bridge.cv2_to_imgmsg(image, encoding="bgr8")

        # Publish the image message
        image_pub.publish(image_msg)

        # Sleep for the remaining time to keep the rate constant
        rate.sleep()


if __name__ == "__main__":
    main()
