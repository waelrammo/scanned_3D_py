import numpy as np
import cv2
import math

# Video Capture
cap = cv2.VideoCapture('video.mp4')

# Get and Print video information
length = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
w = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
print '\n'
print str(length) + ' frames'
print str(fps) + ' fps'
print '(width, height) = (' + str(w) + ', ' + str(h) + ')'
print '\n'

# Create Window
cv2.namedWindow('3D')
cv2.resizeWindow('3D', w, h)

# Get first frame
toggle_lines = False
frame_number = 0
center_line = 279
z = h/2
theta = math.pi/4 # angle between laser and center_line
while True:

	# set up frame
	cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, frame_number)
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	if toggle_lines:

		#center-line
		cv2.line(frame, (center_line, 40), (center_line, h-20), (0, 155, 155), 2)
		
		#offset line
		k = center_line
		maximum = 0
		while k < 379:
			if gray[z][k] > maximum:
				maximum = gray[z][k]
				offset_x_right = k
			k += 1
		k = center_line
		maximum = 0
		while k > 179:
			if gray[z][k] > maximum:
				maximum = gray[z][k]
				offset_x_left = k
			k -= 1
		cv2.line(frame, (offset_x_left, z), (offset_x_right, z), (0, 0, 255), 1)

	#display image
	cv2.imshow('3D', frame)

	#key press check
	key = cv2.waitKey(1)
	if key & 0xFF == ord('['):
		frame_number = (frame_number - 1) % length
		print 'frame_number: ' + str(frame_number)
	if key & 0xFF == ord(']'):
		frame_number = (frame_number + 1) % length
		print 'frame_number: ' + str(frame_number)
	if key & 0xFF == ord('a'):
		center_line -= 1
		print 'center_line: ' + str(center_line)
	if key & 0xFF == ord('d'):
		center_line += 1
		print 'center_line: ' + str(center_line)
	if key & 0xFF == ord('w'):
		z -= 1
		print 'z: ' + str(z)
	if key & 0xFF == ord('s'):
		z += 1
		print 'z: ' + str(z)
	if key & 0xFF == ord('e'):
		radius = (center_line - offset_x_left) / math.sin(theta)
		y = radius * math.cos(theta)
		print 'left (x, y, z) = (' + str(center_line - offset_x_left) + ', ' + str(y) + ', ' + str(h-20-z) + ')'
		radius = (offset_x_right - center_line) / math.sin(theta)
		y = radius * math.cos(theta)
		print 'right (x, y, z) = (' + str(offset_x_right - center_line) + ', ' + str(y) + ', ' + str(h-20-z) + ')'
	if key & 0xFF == ord('t'):
		toggle_lines = not toggle_lines
	if key & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()