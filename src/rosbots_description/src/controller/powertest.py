#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
import serial
import time
port = serial.Serial('/dev/serial0', 38400)

cmdLeft = 127
cmdRight = 255

port.write(bytearray([cmdLeft]))
time.sleep(0.1)
port.write(bytearray([cmdRight]))

time.sleep(2)
port.write(bytearray([64]))
time.sleep(0.1)
port.write(bytearray([192]))
