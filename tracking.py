#refer to
# http://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv
# 2016-4-26
import numpy as np
import cv2
def process(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    #binary = cv2.GaussianBlur(binary, (5,5), 0)
    binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                    cv2.THRESH_BINARY, 11,2)
    return binary

if __name__ == "__main__":
    cap = cv2.VideoCapture(1)
    while True:
	    ret, frame = cap.read()
	    frame = process(frame)
	    cv2.imshow('frame',frame)
	    if cv2.waitKey(1) & 0xFF == ord('q'):
		    break
    cap.release()
    cv2.destroyAllWindows()
