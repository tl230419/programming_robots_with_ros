#!/usr/bin/env python

from math import pi
from fake_sensor import FakeSensor2
import rospy
import tf
from geometry_msgs.msg import Quaternion
import threading

def make_quaternion(angle):
    q = tf.transformations.quaternion_from_euler(0, 0, angle)
    return Quaternion(*q)

def publish_value(value):
    angle = value * 2 * pi / 100.0
    q = make_quaternion(angle)
    pub.publish(q)

if __name__ == '__main__':
    rospy.init_node('fake_sensor')
    pub = rospy.Publisher('angle', Quaternion, queue_size=1)
    sensor = FakeSensor2()
    sensor.register_callback(publish_value)
    sensor.run()