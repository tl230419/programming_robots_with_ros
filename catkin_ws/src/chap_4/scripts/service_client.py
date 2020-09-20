#!/usr/bin/env python

import rospy
from chap_4.srv import WordCount
import sys

rospy.init_node('server_client')
rospy.wait_for_service('word_count')
word_counter = rospy.ServiceProxy('word_count', WordCount)
words = ' '.join(sys.argv[1:])
word_count = word_counter(words)
print words, '->', word_count.count