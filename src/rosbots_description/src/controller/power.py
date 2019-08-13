#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
import serial

port = serial.Serial('/dev/serial0', 38400)

def right_cb(msg):
	cmd = int(64 + msg.data * 63)
	rospy.loginfo('Right: Msg: ' + str(msg) + ' value:' + str(cmd))
	port.write(bytearray([cmd]))
def left_cb(msg):
	cmd = int(192 + msg.data * 63)
	rospy.loginfo('Left: Msg: ' + str(msg) + ' value:' + str(cmd))
	port.write(bytearray([cmd]))

rospy.init_node('power_to_wheels')
rospy.Subscriber('wheel_power_left', Float32, left_cb)
rospy.Subscriber('wheel_power_right', Float32, right_cb)
rospy.spin()
