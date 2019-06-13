
# import system module
import sys
#import os module
import os
# import some PyQt5 modules
import time
import datetime

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

# import Opencv module
import cv2

from ui_main_window import *

class MainWindow(QWidget):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.boxContent = ["normal","abnormal1","abnormal2"]
        self.cameraNum = 2
        self.ui = Ui_Form(self.cameraNum,self.boxContent)
        self.ui.setupUi(self)
        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        self.ui.control_bt.clicked.connect(self.controlTimer)
        self.ui.save_bt.clicked.connect(self.saveImage)
        self.lastImageList = ["",""]
        self.checkSavePath()
        self.capList = []
        self.time = int(round(time.time()*1000))

    def checkSavePath(self):
        for i in self.boxContent:
            if not os.path.exists(i):
                os.makedirs(i)

    # view camera
    def viewCam(self):
        for i in range(self.cameraNum):
            # read image in BGR format
            ret, image = self.capList[i].read()
            #collect image
            self.lastImageList[i] = image
            self.time = int(round(time.time()*1000))
            # convert image to RGB format
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # get image infos
            height, width, channel = image.shape
            step = channel * width
            # create QImage from image
            qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
            # show image in img_label
            self.ui.imageLabelList[i].setPixmap(QPixmap.fromImage(qImg))

    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            if len(self.capList) == 0:
                for i in range(self.cameraNum):
                    print(i)
                    cap = cv2.VideoCapture(i)
                    self.capList.append(cap)
            else:
                for i in range(self.cameraNum):
                    self.capList[i] = cv2.VideoCapture(i)
            # start timer
            self.timer.start(20)
            # update control_bt text
            self.ui.control_bt.setText("Stop")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            for cap in self.capList:
                cap.release()
            
            # update control_bt text
            self.ui.control_bt.setText("Start")

    def saveImage(self):
        for i in range(self.cameraNum):
            boxText = self.ui.boxList[i].currentText()
            cv2.imwrite("%s/%d-%d.png"%(boxText,self.time,i),self.lastImageList[i])
        
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())