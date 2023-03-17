import cv2
import numpy as np
cap =cv2.VideoCapture(0)
back=0
def nothing(x):
    pass

cv2.namedWindow('image')
cv2.createTrackbar('lowh','image',0,179,nothing)
cv2.createTrackbar('highh','image',179,179,nothing)
cv2.createTrackbar('lows','image',0,255,nothing)
cv2.createTrackbar('highs','image',255,255,nothing)
cv2.createTrackbar('lowv','image',0,255,nothing)
cv2.createTrackbar('highv','image',255,255,nothing)
for i in range(20):
    ret,back =cap.read()
cv2.imshow("BACK",back)
while(1):
    ret,frame =cap.read()
    hsv =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowh=cv2.getTrackbarPos('lowh','image')
    highh=cv2.getTrackbarPos('highh','image')
    lows=cv2.getTrackbarPos('lows','image')
    highs=cv2.getTrackbarPos('highs','image')
    lowv=cv2.getTrackbarPos('lowv','image')
    highv=cv2.getTrackbarPos('highv','image')
    lower_limit=np.array([lowh,lows,lowv])
    upper_limit=np.array([highh,highs,highv])
    
    
    
    
    mask=cv2.inRange(hsv,lower_limit,upper_limit)
    
    
    kernel=np.ones((5,5),np.uint8)         
    kernel2=np.ones((11,11),np.uint8)
    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    mask=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel2)
    
    cv2.imshow('mask',mask)
    cv2.imshow('image',hsv)
    mask_inv =cv2.bitwise_not(mask)
    res1=cv2.bitwise_and(frame,frame,mask=mask_inv)
    res2=cv2.bitwise_and(back,back,mask=mask)
    res=res1+res2
#     cv2.imshow("res1",res1)
#     cv2.imshow("res2",res2)
    cv2.imshow("invisibilty",res)
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
