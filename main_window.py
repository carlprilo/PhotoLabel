"""
In this example, we demonstrate how to create simple camera viewer using Opencv3 and PyQt5

Author: Berrouba.A
Last edited: 21 Feb 2018
"""

# import system module
import sys
#import os module
import os
# import some PyQt5 modules
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
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        self.ui.control_bt.clicked.connect(self.controlTimer)

        self.lastImage0 = ""
        self.lastImage1 = ""
        self.checkSavePath()

    def checkSavePath(self):
        pathList = ('./normal','./abnormal1','./abnormal2')
        for i in pathList:
            if not os.path.exists(i):
                os.makedirs(i)

    # view camera
    def viewCam(self):
        # read image in BGR format
        ret, image = self.cap0.read()
        #collect image
        self.lastImage0 = image
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.ui.image_label0.setPixmap(QPixmap.fromImage(qImg))

                # read image in BGR format
        ret, image = self.cap1.read()
        #collect image
        self.lastImage1 = image
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.ui.image_label1.setPixmap(QPixmap.fromImage(qImg))


    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap0 = cv2.VideoCapture(0)
            self.cap1 = cv2.VideoCapture(1)
            # start timer
            self.timer.start(20)
            # update control_bt text
            self.ui.control_bt.setText("Stop")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap0.release()
            self.cap1.release()
            # update control_bt text
            self.ui.control_bt.setText("Start")

            self.saveImage()

    def saveImage(self):
        cv2.imwrite("test0.png",self.lastImage0)
        cv2.imwrite("test1.png",self.lastImage1)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())