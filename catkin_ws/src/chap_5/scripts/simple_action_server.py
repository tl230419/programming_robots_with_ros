#!/usr/bin/env python

import rospy
import time
import actionlib
from chap_5.msg import TimerAction, TimerGoal, TimerResult

def do_timer(goal):
    print('server get goal...')
    start_time = time.time()
    time.sleep(goal.time_to_wait.to_sec())
    result = TimerResult()
    result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
    result.updates_sent = 0
    server.set_succeeded(result)
    print('send result ok...')

rospy.init_node('timer_action_server')
server = actionlib.SimpleActionServer('timer', TimerAction, do_timer, False)
server.start()
print('server started...')
rospy.spin()