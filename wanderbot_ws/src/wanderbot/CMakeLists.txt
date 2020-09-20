cmake_minimum_required(VERSION 2.8.3)
project(wanderbot)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  rospy
  sensor_msgs
)

catkin_package(
    CATKIN_DEPENDS
    geometry_msgs
    sensor_msgs
)

catkin_install_python(PROGRAMS
    scripts/red_light_green_light.py
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/red_light_green_light
)