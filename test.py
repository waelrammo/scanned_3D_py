import numpy as np
import cv2

# Video Capture
cap = cv2.VideoCapture(1)

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

#display image
ret, frame = cap.read()
cv2.imshow('3D', frame)

key = cv2.waitKey(1)
while key & 0xFF != ord('q'):
	key = cv2.waitKey(1)

# Clean UP
cap.release()
cv2.destroyAllWindows()