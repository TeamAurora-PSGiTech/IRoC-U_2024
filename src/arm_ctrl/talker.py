#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16
from arm_ctrl.msg import arm_msg
import sys, select, termios, tty

msg = """
base rotation clk_wise--- 'q'
base rotation anti_clk_wise--- 'z'
link one forward --- 'w'
link one backward --- 'x'
link two forward --- 'e'
link two backward --- 'c'
link three forward --- 'r'
link three backward --- 'v'
gripper clk_wise--- 't'
gripper anti_clk_wise--- 'b'
gripper open ---'y'
gripper close ---'n'
all stop ---'s'
"""
    
 
moveBindings = { 'q','z','w','x','e','c','r','v','t','b','y','n','s'
    }
	
        

    
def getKey(key_timeout):
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], key_timeout)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key



if __name__=="__main__":
    
    settings = termios.tcgetattr(sys.stdin)
    pub = rospy.Publisher("chat", arm_msg, queue_size=10)
    rospy.init_node("talk", anonymous=True)
    rate=rospy.Rate(1)
    key_timeout = None
    s=arm_msg()
    print(msg)

    while(1):
        key = getKey(key_timeout)
        if key in moveBindings:
            if key == 'q':
                s.base_motor=1
            elif key == 'z':
                s.base_motor =-1
            elif key == 'w':
                s.link_1=1
            elif key == 'x':
                s.link_1=-1
            elif key == 'e':
                s.link_2=1
            elif key == 'c':
                s.link_2=-1
            elif key == 'r':
                s.link_3=1
            elif key == 'v':
                s.link_3=-1
            elif key == 't':
                s.waist=1
            elif key == 'b':
                s.waist=-1
            elif key == 'y':
                s.claw=1
            elif key == 'n':
                s.claw=-1
            elif key =='s':
                s.base_motor=0
                s.link_1=0
                s.link_2=0
                s.link_3=0
                s.waist=0
                s.claw=0


            #rospy.loginfo(s)
            pub.publish(s)
            rate.sleep()
            
        else:      
            if key == '' and x == 0 and y == 0 and z == 0 and th == 0:
                continue
            if (key == '\x03'):
                break
