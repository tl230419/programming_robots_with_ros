#!/usr/bin/env python

import rospy
import actionlib
from chap_5.msg import TimerAction, TimerGoal, TimerResult

rospy.init_node('simple_action_client')
client = actionlib.SimpleActionClient('timer', TimerAction)
client.wait_for_server()
goal = TimerGoal()
goal.time_to_wait = rospy.Duration.from_sec(5.0)
client.send_goal(goal)
print('client sent goal...')
client.wait_for_result()
print('get server result, Time elapsed: %f' % (client.get_result().time_elapsed.to_sec()))