# Introduction
This wrapper runs the yolo v5 detection algorithm, and publishes detections on Bounding box format.
Subscribes to /zed/rgb/image_rect_color and publishes to yolo/bbox. 

# Setup

Clone  yolo repo and install requirements.txt in a Python>=3.7.0 environment, including PyTorch>=1.7.

git clone https://github.com/vortexntnu/yolov5.git  
cd yolov5
pip install -r requirements.txt  # install

git clone https://github.com/vortexntnu/yolov5_wrapper.git
git clone https://github.com/vortexntnu/vortex-cv.git

catkin build && . devel/setup.bash
roslaunch roslaunch yolov5_wrapper yolov5_wrapper.launch
rosrun yolov5_wrapper test_node.py (Only for testing)

Go to yolov5_wrapper/config/config_yolov5_wraper.yaml, and check that settings are correct.