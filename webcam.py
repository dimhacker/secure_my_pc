import cv2
import time
import os
 
def  click():
    
    cam = cv2.VideoCapture(0)
    image = cam.read()[1]  # captures image
    count=0
    while 1:
        fname=r'D:\user{}.jpg'.format(count)
        if(os.path.isfile(fname)):
            count+=1
            
        else:
            cv2.imwrite(fname,image)# writes image test.bmp to disk
            break
        
    
click()


