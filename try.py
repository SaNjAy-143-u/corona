import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from scipy.spatial import Delaunay 
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import cv2
import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

root = Tk.Tk()
root.wm_title("Embedding in TK")

img = cv2.imread("/media/sanjay/OS/CORONA/38/DS1025-1039DF038_b.tif")
im_resized = cv2.resize(img, (224, 224))
img = cv2.imread("/media/sanjay/OS/CORONA/38/DS1025-1039DF038_a.tif")
im_resized2 = cv2.resize(img, (224, 224))
images=(im_resized,im_resized2)
f = Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111)
#edges=cv2.Canny(im_resized,224,224)

#points=np.array([[0,50],[0,150],[200,50],[150,150],[50,0],[200,0]])
#tri=Delaunay(points)
#a.triplot(points[:,0],points[:,1],tri.simplices.copy())

# a tk.DrawingArea
# If you put root.destroy() here, it will cause an error if
# the window is closed with the window manager.
class Sticher:
	def stich(self, images,ratio=0.75,threshold=4.0):
		(kpsA,featuresA)=self.detectAndDescribe(images[0])
		(kpsB,featuresB)=self.detectAndDescribe(images[1])
		M=self.matchFeatures(kpsA,kpsB,featuresA,featuresB,ratio,threshold)
		if M is None:
			return None
		(matches,H,status)=M
		result=cv2.warpPerspective(images[0],H,(images[0].shape[1]+images[1].shape[1],images[0].shape[0]))
		result[0:images[1].shape[0],0:images[1].shape[1]]=images[1]
		return result
	def detectAndDescribe(self,image):
		gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
		detector=cv2.FeatureDetector_create("SIFT")
		kps=detector.detect(gray)
		extractor=cv2.DescriptorExtractor_create("SIFT")
		(kps,features)=extractor.compute(gray,kps)
		kps=np.float32([kp.pt for kp in kps])
		return (kps,features)
	def matchKeyPoints(self,kpsA,kpsB,featuresA,featuresB,ratio,threshold):
		matcher=cv2.DescriptorMatcher_create("BruteForce")
		rawMatches=matcher.knnMatch(featuresA,featuresB,2)
		matches=[]
		for m in rawMatches:
			if len(m)==2 and m[0].distance<m[1].distance*ratio:
				matches.append((m[0].trainIdx,m[0].queryIdx))

		if len(matches)>4:
			ptsA=np.float32([kpsA[i] for (_,i)in matches])
			ptsB=np.float32([kpsB[i] for (_,i)in matches])
			(H,status)=cv2.findHomography(ptsA,ptsB,cv2.RANSAC,threshold)
			return (matches,H,status)
		return None

sticher=Sticher()
result=sticher.stich(images)
a.imshow(result)
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

toolbar = NavigationToolbar2TkAgg(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)


def on_key_event(event):
    print('you pressed %s' % event.key)
    key_press_handler(event, canvas, toolbar)

canvas.mpl_connect('key_press_event', on_key_event)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

button = Tk.Button(master=root, text='Quit', command=_quit)
button.pack(side=Tk.BOTTOM)

Tk.mainloop()
