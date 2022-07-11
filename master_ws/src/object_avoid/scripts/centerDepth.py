#!/usr/bin/env python
import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
import numpy as np
from std_msgs.msg import Int32
from object_avoid.msg import Object

def convert_depth_image(ros_image):
	pub = rospy.Publisher("depth", Object , queue_size=10)
	bridge = CvBridge()
	depth_image = bridge.imgmsg_to_cv2(ros_image, desired_encoding="passthrough")
	depth_array = np.array(depth_image, dtype=np.float32)
	center_idx = np.array(depth_array.shape) / 2

	#print ('center depth:', depth_array[center_idx[0], center_idx[1]])
	#print ('center depth:', depth_array[int(center_idx[0])][int(center_idx[1])])
	#print(depth_array[int(center_idx[0])][400:800])
	#print(int(center_depth))
	message = Object()
	message.front = int(depth_array[int(center_idx[0])][int(center_idx[1])])
	message.left = int(depth_array[int(center_idx[0])][int(center_idx[1])-200])
	message.right = int(depth_array[int(center_idx[0])][int(center_idx[1])+200])
	message.left2 = int(depth_array[int(center_idx[0])][0])
	message.right2 = int(depth_array[int(center_idx[0])][1200])
	print(message.front)
	
	pub.publish(message)
	#print (depth_array.shape)

    

def pixel2depth():
	rospy.init_node('pixel2depth',anonymous=True)
	rospy.Subscriber("/camera/aligned_depth_to_color/image_raw", Image,callback=convert_depth_image, queue_size=1)
	rospy.spin()

if __name__ == '__main__':
	pixel2depth()
    
