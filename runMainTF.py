import cv2
import numpy as np
from tensorflow.keras.models import load_model

from adafruit_servokit import ServoKit
import WebcamModule as wM


kit = ServoKit(channels = 16)

#######################################



model = load_model('/home/pi/rcmod/model.h5')
######################################

def preProcess(img):
    img = img[54:120, :, :]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img / 255
    return img

while True:

    img = wM.getImg(True, size=[240, 120])
    img = np.asarray(img)
    img = preProcess(img)
    img = np.array([img])
    steering = float(model.predict(img))
    print(steering)
    
    if steering >= 125 :
        kit.servo[0].angle = 125
    elif steering <= 35:
        kit.servo[0].angle = 35
    else:
        kit.servo[0].angle = steering
    kit.continuous_servo[1].throttle = 0.09
    
    cv2.waitKey(1)