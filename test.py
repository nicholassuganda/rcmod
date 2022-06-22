import cv2
from adafruit_servokit import ServoKit
from time import sleep
import JoyStickModule as jsM

kit = ServoKit(channels =16)
kit.continuous_servo[1].throttle = -1
cam = cv2.VideoCapture(0)

while True:
    joyVal = jsM.getJS()
    if joyVal['axis3'] > 0 and joyVal['axis3'] <=1:
        kit.servo[0].angle = 90 - ((joyVal['axis3']/1)*90)    
    elif joyVal['axis3'] < 0 and joyVal['axis3'] >= -1:
        kit.servo[0].angle = 90 + ((abs(joyVal['axis3']))/1*90)
    elif joyVal['axis3'] == 0:
        kit.servo[0].angle = 90
    if kit.servo[0].angle >= 170:
            kit.servo[0].angle = 170
    if kit.servo[0].angle <= 20:
            kit.servo[0].angle = 20
    print(kit.servo[0].angle)
    if joyVal['axis2'] == -1:
        kit.continuous_servo[1].throttle = 0.09
    elif joyVal['axis2'] == 1:
        kit.continuous_servo[1].throttle = -1

    ret, image = cam.read()
    cv2.imshow('Imagetest',image)
    k = cv2.waitKey(1)
    if k != -1:
        break
cv2.imwrite('/home/pi/testimage.jpg', image)
cam.release()
cv2.destroyAllWindows()