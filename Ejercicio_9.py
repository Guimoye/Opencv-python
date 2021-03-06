import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_orange = np.array([1, 100, 100])
    upper_orange = np.array([21, 255, 255])

    mask = cv2.inRange(hsv, lower_orange, upper_orange)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((5, 5), np.uint8)

    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask, kernel, iterations=1)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)
    #cv2.imshow('Erosion', erosion)
    cv2.imshow('Dilation', dilation)
    cv2.imshow('Opening', opening)
    cv2.imshow('Closing', closing)

    # It is the difference between input image and Opening of the image
    #cv2.imshow('Tophat', tophat)
    #cv2.imshow('Blackhat', blackhat)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()