cmake_minimum_required(VERSION 2.8.3)
project(chap_15)

find_package(catkin REQUIRED COMPONENTS
    rospy
    std_msgs
    geometry_msgs
    message_generation
    actionlib_msgs
)

add_service_files(
    DIRECTORY
    srv
    FILES
    FakeSensor.srv
    Light.srv
)

add_action_files(
    DIRECTORY
    action
    FILES
    Rotation.action
)

generate_messages(
    DEPENDENCIES
    std_msgs
    geometry_msgs
    actionlib_msgs
)

catkin_package(
    CATKIN_DEPENDS
    std_msgs
    geometry_msgs
    message_runtime
    actionlib_msgs
)

catkin_install_python(PROGRAMS
    scripts/service_sensor.py
    scripts/actuator.py
    scripts/service_light_client.py
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/service_sensor
)