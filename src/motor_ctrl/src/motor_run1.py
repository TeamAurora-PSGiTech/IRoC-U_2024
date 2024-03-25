#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from arm_ctrl.msg import arm_msg
import serial
import struct

class TeleopSubscriber():

    def __init__(self):
        rospy.init_node('teleop_wheel')
        self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        self.subscription_speed = rospy.Subscriber('/cmd_vel', Twist, self.listener_callback_speed)
        self.subscription_arm = rospy.Subscriber('/chat', arm_msg, self.listener_callback_arm)
        self.w_r = 0
        self.w_l = 0
        self.wheel_rad = 0.0325 
        self.wheel_sep = 0.295
        self.lowSpeed = 200
        self.highSpeed = 50
        self.speed_ang = 0
        self.speed_lin = 0
        self.serial_msg = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # [motorLF motorLB motorRF motorRB base_rotation link1 link2 link3 gripper_wrist gripper_claw]
        self.base_speed_lock = 25
        self.link_speed = 255
        self.gripper_wrist = 255
        self.gripper_claw = 255

    def listener_callback_speed(self, msg):
        self.speed_ang = msg.angular.z
        self.speed_lin = msg.linear.x
        self.w_r = (self.speed_lin/self.wheel_rad) + ((self.speed_ang*self.wheel_sep)/(2.0*self.wheel_rad))
        self.w_l = (self.speed_lin/self.wheel_rad) - ((self.speed_ang*self.wheel_sep)/(2.0*self.wheel_rad))
        self.MotorL(self.w_l*10)
        self.MotorR(self.w_r*10)
        rospy.loginfo(str(self.serial_msg))
        self.send_float_array(self.serial_msg)

    def listener_callback_arm(self, msg):
        self.serial_msg[4] = (msg.base_motor*self.base_speed_lock)
        self.serial_msg[5] = (msg.link_1*self.link_speed)
        self.serial_msg[6] = (msg.link_2*self.link_speed)
        self.serial_msg[7] = (msg.link_3*self.link_speed)
        self.serial_msg[8] = (msg.waist*self.gripper_wrist)
        self.serial_msg[9] = (msg.claw*self.gripper_claw)
        
        rospy.loginfo(str(self.serial_msg))
        self.send_float_array(self.serial_msg)


    def MotorL(self, PulseWidth):
        self.serial_msg[0] = PulseWidth
        self.serial_msg[1] = PulseWidth

    def MotorR(self, PulseWidth):
        self.serial_msg[2] = PulseWidth
        self.serial_msg[3] = PulseWidth

    def send_float_array(self, data):
        self.packed_data = struct.pack('ffffffffff', *data)
        self.ser.write(self.packed_data)

if __name__ == '__main__':
    try:
        teleopSub = TeleopSubscriber()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
