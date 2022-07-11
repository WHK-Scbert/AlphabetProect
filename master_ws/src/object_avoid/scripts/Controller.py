#!/usr/bin/python

"""
Class for low level control of our car. It assumes ros-12cpwmboard has been
installed
"""
import rospy
from i2cpwm_board.msg import Servo, ServoArray
from geometry_msgs.msg import Twist
import time
from std_msgs.msg import Int32
from object_avoid.msg import Object
from datetime import datetime

class DkLowLevelCtrl():
	def __init__(self):
		rospy.init_node('Controller')
		rospy.Subscriber("depth", Object , callback=self.control, queue_size=1)
		self.ros_pub_servo_array    = rospy.Publisher("/servos_absolute", ServoArray, queue_size=1)
		
		self.command = ServoArray()

		self.command.servos.append(Servo())

		self.now = datetime.now()

		self.current_time = self.now.strftime("%H:%M:%S")


		
	def control(self, Object):
		front = Object.front
		left = Object.left
		right = Object.right
		left2 = Object.left2
		right2 = Object.right2
		#print(str(front))
		'''
		if front <= 500:
			self.command.servos[0].servo = 1
			self.command.servos[0].value = 0.0
			self.ros_pub_servo_array.publish(self.command)
			print("Robot Stopped @ "+ self.current_time)
		elif front > 1200:
			self.command.servos[0].servo = 1
			self.command.servos[0].value = 330.0
			self.ros_pub_servo_array.publish(self.command)
		elif (front <= 1200 and left >= 1200 and right >= 1200): #Facing a Wall but can still turn
			if(left2 > right2):
				self.command.servos[0].servo = 2
				self.command.servos[0].value = 200.0
				self.ros_pub_servo_array.publish(self.command)
				print("Left Turn @ "+ self.current_time)
			else:
				self.command.servos[0].servo = 2
				self.command.servos[0].value = 400.0
				self.ros_pub_servo_array.publish(self.command)
				print("Right Turn @ "+ self.current_time)
		elif (front <= 1200 and left <= 1200 and right >= 1200): #Turn right
				self.command.servos[0].servo = 2
				self.command.servos[0].value = 400.0
				self.ros_pub_servo_array.publish(self.command)
				print("Right Turn @ "+ self.current_time)
		elif (front <= 1200 and left >= 1200 and right <= 1200): #Turn left
				self.command.servos[0].servo = 2
				self.command.servos[0].value = 200.0
				self.ros_pub_servo_array.publish(self.command)
				print("Left Turn @ "+ self.current_time)
		'''
		if front > 2000:
			self.command.servos[0].servo = 2
			self.command.servos[0].value = 300.0
			self.ros_pub_servo_array.publish(self.command)
			print("Roll Out @ "+ self.current_time)
		if (front <= 1200 and left >= 1200 and right >= 1200): #Facing a Wall but can still turn
			if(left2 > right2):
				self.command.servos[0].servo = 2
				self.command.servos[0].value = 200.0
				self.ros_pub_servo_array.publish(self.command)
				print("Left Turn @ "+ self.current_time)
			else:
				self.command.servos[0].servo = 2
				self.command.servos[0].value = 400.0
				self.ros_pub_servo_array.publish(self.command)
				print("Right Turn @ "+ self.current_time)
		elif (front <= 1200 and left <= 1200 and right >= 1200): #Turn right
				self.command.servos[0].servo = 2
				self.command.servos[0].value = 400.0
				self.ros_pub_servo_array.publish(self.command)
				print("Right Turn @ "+ self.current_time)
		elif (front <= 1200 and left >= 1200 and right <= 1200): #Turn left
				self.command.servos[0].servo = 2
				self.command.servos[0].value = 200.0
				self.ros_pub_servo_array.publish(self.command)
				print("Left Turn @ "+ self.current_time)
		
				
			
	def run(self):
		rate = rospy.Rate(10)
		while not rospy.is_shutdown():
			rate.sleep()


if __name__ == "__main__":
	Controller     = DkLowLevelCtrl()
	Controller.run()
