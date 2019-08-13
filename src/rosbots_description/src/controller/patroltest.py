#!/usr/bin/env python

import rospy
import actionlib

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

if __name__ == '__main__':
        rospy.init_node('patrol')

        client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        client.wait_for_server()


