#!/usr/bin/env python

from math import pi
from fake_sensor import FakeSensor2
import rospy
import tf
from geometry_msgs.msg import Quaternion
from threading import Lock, Thread

angle = None

def make_quaternion(angle):
    q = tf.transformations.quaternion_from_euler(0, 0, angle)
    return Quaternion(*q)

def save_value(value):
    with lock:
        global angle
        angle = value * 2 * pi / 100.0

def publish_value():
    while not rospy.is_shutdown():
        with lock:
            if angle:
                q = make_quaternion(angle)
                pub.publish(q)
                print("pub value: ", angle)
        rate.sleep()

if __name__ == '__main__':
    lock = Lock()
    rospy.init_node('fake_sensor')
    pub = rospy.Publisher('angle', Quaternion, queue_size=1)
    sensor = FakeSensor2()
    sensor.register_callback(save_value)
    rate = rospy.Rate(10.0)
    thread = Thread(target=publish_value)
    thread.daemon = True
    thread.start()
    sensor.run()