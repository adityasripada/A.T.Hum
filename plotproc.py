import time
import pyautogui
import os
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
'''
os.system("start test.pde")
time.sleep(1)

pyautogui.keyDown('ctrl')
pyautogui.press('r')
pyautogui.keyUp('ctrl')
time.sleep(3)
'''
i = 1

while True:
	pyautogui.press('r')
	time.sleep(0.01)
	f = open('angles.txt','r')
	z = f.readlines()
	f.close()
	points = []
	for point in z:
		y = np.array([float((x)) for x in point.split(',')])
		points.append(y)
	v1 = points[1] - points[0]
	v2 = points[2] - points[1]
	v3 = points[3] - points[2]
	v4 = points[4] - points[0]
	v5 = points[5] - points[4]
	v6 = points[6] - points[5]
	if i ==1:
		ax.plot(v1,v2,zs = v3)
	else:
		ax.plot(v2,v3,zs = v4)
	plt.show(block = False)
	#Axes3D.plot()
	print "yup"
	i *= -1
	time.sleep(1)
	plt.clf()