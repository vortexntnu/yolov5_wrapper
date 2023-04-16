#!/usr/bin/python3

import rospy

from sensor_msgs.msg import Image
from cv_msgs.msg import BBox, BBoxes
from cv_bridge import CvBridge
import yolo_detector


"""

"""


class YoloWrapperNode:
    def __init__(self):
        self.detector = yolo_detector.YOLOv5Detector()

        rospy.init_node("yolov5_wrapper_node")
        self.image_sub = rospy.Subscriber(
            "/zed/rgb/image_rect_color", Image, self.img_cb
        )
        self.bbox_pub = rospy.Publisher("yolo/bbox", BBoxes, queue_size=10)

        self.seq = 0
        self.frame_id = "zed2_left_camera_sensor"
        self.bridge = CvBridge()

        self.approval_treashold = 0.5

    def img_cb(self, msg):
        img = self.unpack_img_msg(msg)
        results = self.detector.perform_inference(img)
        print(results)

        if len(results.xyxy[0]) > 0:
            self.publish_approved_results(results)

    def publish_approved_results(self, results):
        bboxes = self.pack_approved_BBoxes_msg(results)
        self.bbox_pub.publish(bboxes)

    def unpack_img_msg(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
        except Exception as e:
            print(e)
            return

        return cv_image

    def pack_approved_BBoxes_msg(self, results):
        bbox_list_msg = BBoxes()

        bbox_list_msg.header.stamp = rospy.Time.now()
        bbox_list_msg.header.frame_id = self.frame_id
        bbox_list_msg.header.seq = self.seq
        self.seq += 1

        for det in results.xyxy[0]:
            bbox_msg = BBox()

            bbox_msg.probability =det[4].item()
            bbox = det[:4]
            bbox = bbox.int()
            x1, y1, x2, y2 = bbox
            bbox_msg.xmin = x1.item()
            bbox_msg.ymin = y1.item()
            bbox_msg.xmax = x2.item()
            bbox_msg.ymax = y2.item()
            bbox_msg.z = 1000000.0  #  z value will be set in Point cloud processing

            bbox_msg.id = 0  #
            bbox_msg.Class = str(
                det[5].item()
            )  # OBS: should be possible to find the actuall string corresponding to the number

            bbox_list_msg.bounding_boxes.append(bbox_msg)

        return bbox_list_msg


if __name__ == "__main__":
    try:
        wrapper = YoloWrapperNode()
        rospy.spin()

    except rospy.ROSInterruptException:
        pass
