import crop
import Sticher
import Input
import dialog
import warp
import cv2
import re
from PIL import Image
def repl(m):
	current=m.group(1)
	return chr(ord(current)+1)+m.group(2)
dstPoints=[]
srcPoints=[]
srcImg=[]
imagelocB="/media/sanjay/OS/CORONA/37/DS1025-1039DF037_b.tif"
imagelocC="/media/sanjay/OS/CORONA/37/DS1025-1039DF037_c.tif"
imagelocD="/media/sanjay/OS/CORONA/37/DS1025-1039DF037_d.tif"
sticher=Sticher.Sticher()
#(srcLoc,dstLoc)=Input.inputWindow()
srcLoc="/media/sanjay/OS/CORONA/37/DS1025-1039DF037_a.tif"
dstLoc="/media/sanjay/OS/CORONA/37/"
#imageLocB=re.sub(r"(\w)(\.tif)",repl,srcLoc)
#imageLocC=re.sub(r"(\w)(\.tif)",repl,srcLoc)
#imageLocD=re.sub(r"(\w)(\.tif)",repl,srcLoc)
imageA=cv2.imread(srcLoc)
imageB=cv2.imread(imagelocB)
imageC=cv2.imread(imagelocC)
imageD=cv2.imread(imagelocD)
imageA=cv2.resize(imageA,(1500,1500))
imageB=cv2.resize(imageB,(1500,1500))
imageC=cv2.resize(imageC,(1500,1500))
imageD=cv2.resize(imageD,(1500,1500))
(resultRight,vis)=sticher.stich(imageA,imageB,showMatches=True)
(resultLeft,vis2)=sticher.stich(imageC,imageD,showMatches=True)
cv2.imwrite(dstLoc+"stichedleft.tif",resultLeft)
cv2.imwrite(dstLoc+"stichedright.tif",resultRight)
cv2.imshow("result",resultRight)
cv2.imshow("visual",vis)
cv2.waitKey(0)
cv2.destroyAllWindows()
#ToDo: add crop part here
#resultRight=crop.startCropping(resultRight)
#resultLeft=crop.startCropping(resultLeft)
result=sticher.stich(resultRight,resultLeft,showMatches=False)
result=cv2.resize(result,(4000,1000))
cv2.imwrite(dstLoc+"stiched.tif",result)
stiched=Image.open(dstLoc+"stiched.tif")
stiched.show()
