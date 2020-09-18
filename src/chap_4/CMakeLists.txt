cmake_minimum_required(VERSION 2.8.3)
project(chap_4)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
)

add_service_files(
    DIRECTORY
    srv
    FILES
    WordCount.srv
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
  scripts/service_server.py
  scripts/service_client.py
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/service_server_client
)

install(FILES
  scripts/service_server_client.launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/service_server_client
)