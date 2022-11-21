import cv2

capture = cv2.VideoCapture("files/times_square.mp4",cv2.CAP_DSHOW)
if not capture.isOpened():
    raise IOError("Camera not opened")
   
capture.set(3,840)#width has an id of 3, set px to 640
capture.set(4,600)#height has an id of 4, set px to 480

#object detection from a stable camera
object_detector= cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=40)
# idnetify the moving objects from the background


while True:

    sucess, frame = capture.read()
    height,width,_=frame.shape
  
    
  
    if(sucess):
        # print(height,width)
        #extract a region of interest'
        roi = frame[250:700,400:1200]
        mask=object_detector.apply(roi)
        #clean the mask from grey shadows
        _,mask = cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
        #use findContours to find the objects boundaries
        contours ,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            #calculate area and remove small objects masks
           area = cv2.contourArea(cnt)
           if area > 300:
            #cv2.drawContours(roi,[cnt],-1,(0,255,0),2) 
            #draw rectangle arounf the contour
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(roi,(x,y),(x + w, y + h),(0,255,0),3)
        cv2.imshow("frame",roi)
       
       # cv2.imshow("Mask",mask) # identified objects are in white, black is the background
    else:
        break
    
    if cv2.waitKey(30) & 0xFF == ord('q'):
            break
capture.release()
cv2.destroyAllWindows()


