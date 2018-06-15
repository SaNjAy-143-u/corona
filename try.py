import matplotlib
matplotlib.use('TkAgg')
import dialog
import numpy as np
import dialog
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
srclist=[]
dstlist=[]
root = Tk.Tk()
root.wm_title("Embedding in TK")

def addToSrc(x,y):
    srclist.append((x,y))

def onclick(event):
    addToSrc(event.xdata, event.ydata)
    dstlist.append(dialog.getLatLong())

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent

def printsrc():
    print (srclist,dstlist)                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate



img = cv2.imread("/media/sanjay/OS/CORONA/38/DS1025-1039DF038_a.tif")
im_resized2 = cv2.resize(img, (224, 224))
f = Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111)
#edges=cv2.Canny(im_resized,224,224)

#points=np.array([[0,50],[0,150],[200,50],[150,150],[50,0],[200,0]])
#tri=Delaunay(points)
#a.triplot(points[:,0],points[:,1],tri.simplices.copy())

# a tk.DrawingArea
# If you put root.destroy() here, it will cause an error if
# the window is closed with the window manager.

a.imshow(im_resized2)
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

toolbar = NavigationToolbar2TkAgg(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
f.canvas.mpl_connect('button_press_event', onclick)


button = Tk.Button(master=root, text='Quit', command=_quit)
button.pack(side=Tk.BOTTOM)
button2=Tk.Button(master=root,text='print list',command=printsrc)
button2.pack(side=Tk.TOP)
Tk.mainloop()




