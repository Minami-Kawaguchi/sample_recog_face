#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import time
from std_msgs.msg import String
from vino_people_msgs.msg import AgeGenderStamped,AgeGender

class Recog_face:
	def __init__(self):
		self.age=0
		rospy.Subscriber('/ros_openvino_toolkit/age_genders_Recognition', AgeGenderStamped, self.humanCB)
	
	def humanCB(self,data):
		self.age=data.objects[0].age
		
		
if __name__ == '__main__':
	rospy.init_node('Face',anonymous=True)
	human=Recog_face()
	#年齢の読み込みに時間がかかることがあるので待つ
	time.sleep(2)
	print(human.age)

