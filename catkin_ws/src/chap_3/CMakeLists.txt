cmake_minimum_required(VERSION 2.8.3)
project(chap_3)

find_package(catkin REQUIRED COMPONENTS
    rospy
    std_msgs
    message_generation
)

add_message_files(
    DIRECTORY
    msg
    FILES
    Complex.msg
)

generate_messages(
    DEPENDENCIES
    std_msgs
)

catkin_package(CATKIN_DEPENDS
    std_msgs
    message_runtime
)

catkin_install_python(PROGRAMS
  scripts/3_1_topic_publisher_subscriber/topic_publisher.py
  scripts/3_1_topic_publisher_subscriber/topic_subscriber.py
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/3_1_topic_publisher_subscriber
)

install(FILES
  scripts/3_1_topic_publisher_subscriber/README
  scripts/3_1_topic_publisher_subscriber/3_1_publisher_subscriber.launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/3_1_topic_publisher_subscriber
)

catkin_install_python(PROGRAMS
  scripts/3_5_message_publisher_subscriber/message_publisher.py
  scripts/3_5_message_publisher_subscriber/message_subscriber.py
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/3_5_message_publisher_subscriber
)

install(FILES
  scripts/3_5_message_publisher_subscriber/README
  scripts/3_5_message_publisher_subscriber/3_5_publisher_subscriber.launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/3_5_message_publisher_subscriber
)

catkin_install_python(PROGRAMS
  scripts/3_7_double/double.py
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/3_7_double
)