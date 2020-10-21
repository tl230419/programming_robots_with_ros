cmake_minimum_required(VERSION 2.8.3)
project(chap_15)

find_package(catkin REQUIRED COMPONENTS
    rospy
    std_msgs
    geometry_msgs
    message_generation
)

add_service_files(
    DIRECTORY
    srv
    FILES
    FakeSensor.srv
)

generate_messages(
    DEPENDENCIES
    std_msgs
    geometry_msgs
)

catkin_package(
    CATKIN_DEPENDS
    std_msgs
    geometry_msgs
    message_runtime
)

catkin_install_python(PROGRAMS
    scripts/service_sensor.py
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/service_sensor
)