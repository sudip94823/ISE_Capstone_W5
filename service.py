#! /usr/bin/env python

import rospy
from std_msgs.msg import String
from my_package.srv import Alert, AlertResponse

def handle_alert(req):
    rospy.loginfo('Motion detected in %s' % req.location)
    # Send alert to caregiver (e.g. via email or SMS)
    return AlertResponse(True)

if __name__ == '__main__':
    rospy.init_node('alert_service')
    rospy.Service('alert', Alert, handle_alert)
    rospy.spin()
