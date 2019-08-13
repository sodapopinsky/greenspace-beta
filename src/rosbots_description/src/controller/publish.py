import rospy
from geometry_msgs.msg import Twist

rospy.init_node('test_publisher', anonymous=True)

t = Twist()

velocity_publisher = rospy.Publisher('/part2_cmr/cmd_vel', Twist, queue_size=10)
t.linear.x = 1.0
t.angular.z = 0.0

velocity_publisher.publish(t)
