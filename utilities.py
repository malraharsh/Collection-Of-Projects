import cv2
import numpy as np

def show(img):
    cv2.imshow('title', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def label_contour(img, cnt, text, color, fontsize = 1.0, thickness = 2):
    M = cv2.moments(cnt)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    
    cv2.drawContours(img, [cnt], -1, color, thickness)
    shift = (len(text) * fontsize) // 2 * 15 # to print to center , shifting along x
    cv2.putText(img, text, (cx-int(shift), cy), cv2.FONT_HERSHEY_SIMPLEX, fontsize, (255, 255, 255), 2)
    
def resize_to_fit(img):
    return cv2.resize(img, (640, 480))   #(400, 300)