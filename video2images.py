"""
Created on Tue Mar  9 11:27:58 2020

@author: ymerabet
"""

#### Video to images frames

import cv2

### Set your output folder
output_folder = "/home/ymerabet/Bureau/images/"

# Opens the Video file ## change to your video path 
cap = cv2.VideoCapture('/home/ymerabet/Bureau/video/video1.mp4')
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    if i % 20 == 0: # this is the line I added to make it only save one frame every 20
        cv2.imwrite(output_folder+'frame'+str(i)+'.jpg',frame)
    i+=1

cap.release()
cv2.destroyAllWindows()