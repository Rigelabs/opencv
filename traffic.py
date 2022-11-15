import torch
import cv2
from matplotlib import pyplot as plt
import numpy as np

#load model from pytorch hub yolov5 models
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

#test by loading an image using a link

#img = "files/kenyan_traffic.jpg"
#results=model(img)
#results.print()
#show the image
#plt.imshow(np.squeeze(results.render()))
#plt.show()

#use cv2 use the webcam
capture =cv2.VideoCapture(0)
if  not capture.isOpened:
    raise IOError("Camera not opened")
while True:
    success, frame = capture.read()
    if(success == False):
        print("Operation failed")
        break
    #load the results by running the model and feed the frame

    results = model(frame)
    #use the results.render to get the arrays of the observed objects
    cv2.imshow("Yolo", np.squeeze(results.render()))

    if cv2.waitKey(30) & 0xFF == ord('q'):
            break
capture.release()
cv2.destroyAllWindows()
