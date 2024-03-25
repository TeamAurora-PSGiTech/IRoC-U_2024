#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16
from arm_ctrl.msg import arm_msg
  
def listner():
    rospy.init_node('listen', anonymous=True
)
    rospy.Subscriber("chat", arm_msg, hear)
    rospy.spin()

def hear(message):

    		
    print(message.base_motor)

   


if __name__=="__main__":
    
    listner()
    
