cmake_minimum_required(VERSION 2.8.3)
project(chap_3)

find_package(catkin REQUIRED COMPONENTS rospy std_msgs)

catkin_package(CATKIN_DEPENDS std_msgs)

# do not wildcard install files since the root folder of the package will contain a debian folder for releasing
catkin_install_python(PROGRAMS
  scripts/topic_publisher.py
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/topic_publisher
)
install(FILES
  scripts/README
  scripts/publisher_subscriber.launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/topic_publisher
)