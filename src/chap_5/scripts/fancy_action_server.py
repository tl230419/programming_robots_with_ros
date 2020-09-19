#!/usr/bin/env python

import rospy
import time
import actionlib
from chap_5.msg import TimerAction, TimerGoal, TimerResult, TimerFeedback

def do_timer(goal):
    print('server get goal...')
    start_time = time.time()
    update_count = 0

    if goal.time_to_wait.to_sec() > 60.0:
        result = TimerResult()
        result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
        result.updates_sent = update_count
        server.set_aborted(result, "Timer aborted due to too-long wait")
        print('send result ok...')
        return

    while (time.time() - start_time) < goal.time_to_wait.to_sec():
        if server.is_preempt_requested():
            result = TimerResult()
            result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
            result.updates_sent = update_count
            server.set_preempted(result, "Timer preempted")
            print('send result ok...')
            return

        feedback = TimerFeedback()
        feedback.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
        feedback.time_remaining = goal.time_to_wait - feedback.time_elapsed
        server.publish_feedback(feedback)
        update_count += 1
        print('send feedback ok...%d' % update_count)
        time.sleep(1.0)

    result = TimerResult()
    result.time_elapsed = rospy.Duration.from_sec(time.time() - start_time)
    result.updates_sent = update_count
    server.set_succeeded(result, "Timer completed successfully")
    print('send result ok...')

rospy.init_node('timer_action_server')
server = actionlib.SimpleActionServer('timer', TimerAction, do_timer, False)
server.start()
print('server started...')
rospy.spin()