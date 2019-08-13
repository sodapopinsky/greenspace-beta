#!/usr/bin/env python
#rosrun teleop_twist_keyboard teleop_twist_keyboard.py /cmd_vel:=/part2_cmr/cmd_vel

import rospy

from controller.supervisor import Supervisor
    
def main():
    rospy.init_node('part2_cmr', anonymous=False)
    
    supervisor = Supervisor()
    
    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        supervisor.execute()
        rate.sleep()


if __name__ == '__main__':
    main()
