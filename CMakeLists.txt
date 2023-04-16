cmake_minimum_required(VERSION 3.0.2)
project(yolov5_wrapper)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  cv_bridge
  cv_msgs
  rospy
  sensor_msgs
  std_msgs
)

find_package(OpenCV REQUIRED)

# set(Torch_DIR /home/vortex/.local/lib/python3.8/site-packages/torch/share/cmake/Torch)
# find_package(Torch REQUIRED)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES yolov5_wrapper
#  CATKIN_DEPENDS cv_bridge cv_msgs rospy sensor_msgs std_msgs
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)


include_directories(${OpenCV_INCLUDE_DIRS})
# include_directories(${Torch_INCLUDE_DIRS})



