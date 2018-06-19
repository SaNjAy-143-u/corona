# import the necessary packages
import sys
sys.path.append("/home/sanjay")
import Sticher
import argparse
import imutils
import cv2
import crop
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True,
help="path to the first image")
ap.add_argument("-s", "--second", required=True,
help="path to the second image")
ap.add_argument("-t", "--third", required=True,
help="path to the third image")
ap.add_argument("-e", "--fourth", required=True,
help="path to the fourth image")
args = vars(ap.parse_args())
# load the two images and resize them to have a width of 400 pixels
# (for faster processing)
imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"])
imageC = cv2.imread(args["third"])
imageD = cv2.imread(args["fourth"])
imageA = imutils.resize(imageA, 1500,1500)
imageB = imutils.resize(imageB, 1500,1500)
imageC = imutils.resize(imageC, 1500,1500)
imageD = imutils.resize(imageD, 1500,1500)
 
# stitch the images together to create a panorama
stitcher =Sticher.Sticher()
(result1, vis) = stitcher.stich(imageA, imageB, showMatches=True)
result1=crop.startCropping(result1)
'''
(result2, vis) = stitcher.stich(imageC,imageD, showMatches=True)
result2=crop.startCropping(result2)
(result, vis) = stitcher.stich(result1, result2, showMatches=True)
# show the images
#cv2.imshow("Image A", imageA)
#cv2.imshow("Image B", imageB)
cv2.imshow("Keypoint Matches", vis)
'''
cv2.imshow("Result", result1)

cv2.waitKey(0)