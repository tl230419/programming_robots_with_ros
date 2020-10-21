#!/usr/bin/env python

import rospy
from chap_15.srv import Light, LightRequest

if __name__ == '__main__':
    rospy.init_node('service_light_client')
    rospy.wait_for_service('/fake/light')
    light = rospy.ServiceProxy('/fake/light', Light)
    req = LightRequest()
    req.on = "true"
    print("start to call")
    resp = light(req)
    print("finish to call")
    # if resp.status:
    #     print("Open ok.")
    # else:
    #     print("Open failed.")