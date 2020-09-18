#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

rospy.init_node('double')

def callback(msg):
    print "get msg: ", msg.data
    doubled = Int32()
    doubled.data = msg.data * 2

    pub.publish(doubled)
    print "publish msg: ", doubled.data

sub = rospy.Subscriber('number', Int32, callback)
pub = rospy.Publisher('doubled', Int32)

rospy.spin()