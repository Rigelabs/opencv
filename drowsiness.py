import torch
import cv2
from matplotlib import pyplot as plt
import numpy as np
import uuid
import os
import time


# take images from the webcam and add to classifier
IMAGES_PATH = os.path.join('files','data')
labels=["awake","drowsy"]
number_imgs=20

capture =cv2.VideoCapture(0)
if  not capture.isOpened:
    raise IOError("Camera not opened")
#loop through labels
"""for label in labels:
    print("Collecting images for {}".format(label))
    time.sleep(5)
    #loop through images
    for img_num in range(number_imgs):
        print("Collecting images for {}, image number {}".format(label,img_num))
        success, frame = capture.read()
        if(success == False):
            print("Operation failed")
            break
        img_name = os.path.join(IMAGES_PATH,label+'.'+str(uuid.uuid1())+'.jpg')
        cv2.imwrite(img_name,frame)
        cv2.imshow("Image Collection",frame)
        time.sleep(3)
    """    
        #Label Annotation
        #clone the labelsImg from fit github and run 
            #cd labelImg && pyrcc5 -o libs/resources.py resources.qrc
            #cb labelImg and run python labelImg.py
        #Model Retraining
        #create the dataset.yaml for training configuration and add the labels as in classes.txt
        #cd yolov5 && python train.py --img 320 --batch 10 --epochs 5 --data dataset.yaml --weights yolov5s.pt --workers 2

        
    #load the custom model
while True:
    model = torch.hub.load('ultralytics/yolov5','custom',path="yolov5/runs/train/exp6/weights/last.pt",force_reload=True)
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
