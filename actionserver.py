#! /usr/bin/env python

import rospy
import actionlib

from my_package.msg import MotionDetectionAction, MotionDetectionFeedback, MotionDetectionResult

class MotionDetectionServer(object):
    _feedback = MotionDetectionFeedback()
    _result = MotionDetectionResult()

    def __init__(self, name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, MotionDetectionAction, execute_cb=self.execute_cb, auto_start = False)
        self._as.start()

    def execute_cb(self, goal):
        # Process goal and detect motion using OpenCV
        # Publish message to alert service
        if motion_detected:
            rospy.loginfo('Motion detected in %s' % goal.location)
            self._result.success = True
            self._as.set_succeeded(self._result)
        else:
            rospy.loginfo('No motion detected')
            self._result.success = False
            self._as.set_succeeded(self._result)

if __name__ == '__main__':
    rospy.init_node('motion_detection_server')
    server = MotionDetectionServer(rospy.get_name())
    rospy.spin()
