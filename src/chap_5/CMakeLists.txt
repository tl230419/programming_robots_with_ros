cmake_minimum_required(VERSION 2.8.3)
project(chap_5)

find_package(catkin REQUIRED COMPONENTS
    actionlib
    actionlib_msgs
    rospy
    std_msgs
)

add_action_files(
    DIRECTORY
    action
    FILES
    Timer.action
)

generate_messages(
    DEPENDENCIES
    actionlib_msgs
    std_msgs
)

catkin_package(
    CATKIN_DEPENDS
    std_msgs
    actionlib_msgs
)

catkin_install_python(PROGRAMS
    scripts/simple_action_server.py
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/simple_action_server
)