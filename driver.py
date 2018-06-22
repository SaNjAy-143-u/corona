import sys
from PyQt5 import QtGui, QtCore, QtWidgets
import cv2
from PIL import Image
import warp

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


import random
import dialog

class Window(QtWidgets.QDialog):
    global srclist, dstlist
    srclist=[]
    dstlist=[]

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # a figure instance to plot on
        self.figure = Figure(figsize=(5, 4), dpi=100)

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)
        imgLoc = "C:\\Users\\Naman\\Desktop\\images.jpg"
        img = Image.open(imgLoc)

        global im_resized
        im_resized = img.resize((5000, 5000), Image.ANTIALIAS)

        # Just some button connected to `plot` method
        self.proceedBtn = QtWidgets.QPushButton('Proceed')
        self.proceedBtn.clicked.connect(self.startWarping)

        self.quitBtn = QtWidgets.QPushButton('Quit')
        self.quitBtn.clicked.connect(self._quit)

        self.printBtn = QtWidgets.QPushButton('Print List')
        self.printBtn.clicked.connect(self.printsrc)

        ax = self.figure.add_subplot(111)

        cid=self.figure.canvas.mpl_connect('button_press_event', self.onclick)

        ax.imshow(im_resized)


        layout = QtWidgets.QVBoxLayout()

        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        layout.addWidget(self.printBtn)
        layout.addWidget(self.proceedBtn)
        layout.addWidget(self.quitBtn)
        self.setLayout(layout)
        dstImg = Image.new(img.mode, (5000, 5000))

        # self.canvas.show()



        # set the layout

    def onclick(self, event):
        global dstlist
        self.addToSrc(event.xdata, event.ydata)
        dstlist.append(dialog.getLatLong())

    def addToSrc(self, x,y):
        srclist.append((x,y))


    def _quit(self):
        main.quit()     # stops mainloop
        main.destroy()  # this is necessary on Windows to prevent

    def printsrc(self):
        print(srclist,dstlist)
        # Fatal Python Error: PyEval_RestoreThread: NULL tstate

    def startWarping(self):
       global dstImg
       dstImg=warp.Warping(im_resized,srclist,dstImg,dstlist)
       dstImg.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())