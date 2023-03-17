import cv2
import numpy as np
def func(x):
    pass

cap=cv2.VideoCapture(r"ball detection.mp4")



#cv2.namedWindow("WIN")
#cv2.resizeWindow("WIN",(300,400))

#cv2.createTrackbar("LH","WIN",0,255,func)
#cv2.createTrackbar("LS","WIN",0,255,func)
#cv2.createTrackbar("LV","WIN",0,255,func)

#cv2.createTrackbar("HH","WIN",0,255,func)
#cv2.createTrackbar("HS","WIN",0,255,func)
#cv2.createTrackbar("HV","WIN",0,255,func)


while 1:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(500,480))
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #lh=cv2.getTrackbarPos("LH","WIN")
    #ls=cv2.getTrackbarPos("LS","WIN")
    #lv=cv2.getTrackbarPos("LV","WIN")
    
    #hh=cv2.getTrackbarPos("HH","WIN")
    #hs=cv2.getTrackbarPos("HS","WIN")
    #hv=cv2.getTrackbarPos("HV","WIN")
    
    lower=np.array([0,91,162])
    upper=np.array([14,255,239])
    
     lower1=np.array([100,21,69])
    upper1=np.array([4,63,219])
    #lower=np.array([lh,ls,lv])
    #upper=np.array([hh,hs,hv])
    
    
    
    th=cv2.inRange(hsv,lower,upper)
    
    contours,_=cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    if(len(contours)!=0):
        max_cnt=max(contours,key=cv2.contourArea)
        area=cv2.contourArea(max_cnt)
        if(area>150):
            #frame=cv2.drawContours(frame,[max_cnt],0,(0,255,0),3)
            x,y,w,h=cv2.boundingRect(max_cnt)
            frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            frame=cv2.putText(frame,"ORANGE",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2,cv2.LINE_AA)
            frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            frame=cv2.putText(frame,"PINK",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,1,(255,182,190),2,cv2.LINE_AA)
    
    #cv2.imshow("WIN1",th)
    cv2.imshow("WIN2",frame)
    if(cv2.waitKey(1)==ord("q")):
        break
cap.release()
cv2.destroyAllWindows()
