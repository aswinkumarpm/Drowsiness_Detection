import cv2
import os

import numpy as np
import time

cas_path = os.getcwd()
eye_path = os.getcwd()
two_eyes_path = os.getcwd()

cas_path += "/haarcascade_frontalface_alt.xml"
eye_path += "/haarcascade_eye_tree_eyeglasses.xml"
two_eyes_path += "/haarcascade_eye.xml"


faceCascade = cv2.CascadeClassifier(cas_path)
eyesCascade = cv2.CascadeClassifier(eye_path)
twoeyesCascade = cv2.CascadeClassifier(two_eyes_path)

class VideoCamera(object):

    def __init__(self):

        self.status = "Sharing ?"
        self._image = np.zeros((100,200))
        self.video = cv2.VideoCapture(0)
        (self.video).set(3, 200)
        (self.video).set(4, 160)
    #success, self._image = self.video.read()
    # If you decide to use video.mp4, you must have this file in the folder
    # as the main.py.
    # self.video = cv2.VideoCapture('video.mp4')

def __del__(self):
    self.video.release()
def get_frame(self):
    global s
    s = ''
    global string
    string = ''
    success, image = self.video.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )


    count  = 0

    # for (x, y, w, h) in faces:
    #     cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)
    #     roi_gray = gray[y:y+h, x:x+w]
    #     roi_color = image[y:y+h, x:x+w]
    #     eyes = eyesCascade.detectMultiScale(roi_gray)
    #     if eyes is not():
    #         for (ex,ey,ew,eh) in eyes:
    #             cv2.rectangle(roi_color,(ex -10 ,ey - 10),(ex+ew + 10,ey+eh + 10),(0,255,0),2)
    #             twoeyes = twoeyesCascade.detectMultiScale(roi_gray)
    #             firsttime = 1
    #             if twoeyes is not():
    #                 for (exx,eyy,eww,ehh) in twoeyes:
    #                     cv2.rectangle(roi_color,(exx-5 ,eyy -5  ),(exx+eww -5,eyy+ehh -5 ),(0,0, 255),2)
    #
    #
    # ret, jpeg = cv2.imencode('.jpg', image)
    # self.string = jpeg.tostring()
    # self._image = image
    # return jpeg.tostring()

    while True:
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)

                roi_gray = gray[y:y+h, x:x+w]
                roi_color = image[y:y+h, x:x+w]
                eyes = eyesCascade.detectMultiScale(roi_gray)
                if eyes is not():
                    for (ex,ey,ew,eh) in eyes:
                        cv2.rectangle(roi_color,(ex -10 ,ey - 10),(ex+ew + 10,ey+eh + 10),(0,255,0),2)
                        twoeyes = twoeyesCascade.detectMultiScale(roi_gray)
                        checkyeys = 0
                        if twoeyes is not():
                            for (exx,eyy,eww,ehh) in twoeyes:
                                checkyeys = 0
                                cv2.rectangle(roi_color,(exx-5 ,eyy -5  ),(exx+eww -5,eyy+ehh -5 ),(0,0, 255),2)
                        else:
                            #when eyes close
                            for i in range(10):
                                time.sleep(1)
                                if i % 3 == 0:
                                    #eyes close in 3 seconds
                                    print("Warning")
            ret, jpeg = cv2.imencode('.jpg', image)
            self.string = jpeg.tostring()
            self._image = image
            return jpeg.tostring()

def GetBw(self):
    image = self._image
    ret, jpeg = cv2.imencode('.jpg', image)
    self.string = jpeg.tostring()
    return jpeg.tostring()

