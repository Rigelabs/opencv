import cv2

camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
if not camera.isOpened():
    raise IOError("Cannot open camera")
    
camera.set(3,640)#width has an id of 3, set px to 640
camera.set(4,480)#height has an id of 4, set px to 480
while True:
    success,img =camera.read()
    if(success):
        cv2.imshow("Video",img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        print("Operation failed")
        break