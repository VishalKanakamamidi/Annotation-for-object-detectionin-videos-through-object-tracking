# USAGE
# python multi_object_tracking.py --video videos/soccer_01.mp4 --tracker csrt

# import the necessary packages
from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import PIL
from shutil import copyfile
import string
classes = input("class-name?")
version = input("version?")
import os
directory = "items/"+classes
flagg = input("Again?")
if flagg == "y":
	os.mkdir(directory)
	os.mkdir(directory+"/frames")
	os.mkdir(directory+"/annot")


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", type=str,
	help="path to input video file")
ap.add_argument("-t", "--tracker", type=str, default="kcf",
	help="OpenCV object tracker type")
args = vars(ap.parse_args())

# initialize a dictionary that maps strings to their corresponding
# OpenCV object tracker implementations
OPENCV_OBJECT_TRACKERS = {
	"csrt": cv2.TrackerCSRT_create,
	"kcf": cv2.TrackerKCF_create,
	"boosting": cv2.TrackerBoosting_create,
	"mil": cv2.TrackerMIL_create,
	"tld": cv2.TrackerTLD_create,
	"medianflow": cv2.TrackerMedianFlow_create,
	"mosse": cv2.TrackerMOSSE_create
}

# initialize OpenCV's special multi-object tracker
trackers = cv2.MultiTracker_create()

# if a video path was not supplied, grab the reference to the web cam
if not args.get("video", False):
	print("[INFO] starting video stream...")
	vs = VideoStream(src=0).start()
	time.sleep(1.0)
	count = 0
	flag = 1

# otherwise, grab a reference to the video file
else:
	vs = cv2.VideoCapture(args["video"])
	

# loop over frames from the video stream
totalp = 0
while True:
	# grab the current frame, then handle if we are using a
	# VideoStream or VideoCapture object
	frame = vs.read()
	frame = frame[1] if args.get("video", False) else frame
	

	# check to see if we have reached the end of the stream
	if frame is None:
		break

	# resize the frame (so we can process it faster)
	# frame = imutils.resize(frame, width=600)

	# grab the updated bounding box coordinates (if any) for each
	# object that is being tracked
	(success, boxes) = trackers.update(frame)


	# loop over the bounding boxes and draw then on the frame
	for box in boxes:
		(x, y, w, h) = [int(v) for v in box]
		print(x, y, w, h)
		
		
		

		if (x>0 and y>0 and (x+w)>0 and (y+h)>0):
			cv2.imwrite(directory+"/frames"+"/frame"+version+classes+str(count)+".jpg",frame)
			copyfile("anno.xml",directory+"/"+ "annot/frame"+version+classes+str(count)+".xml")
			s = open(directory+"/"+"annot/frame"+version+classes+str(count)+".xml").read()
			s = s.replace("jpg","frame"+version+classes+str(count)+".jpg")
			s= s.replace("cream",classes)

			s = s.replace("xmini",str(x))
			s = s.replace("ymini",str(y))
			s = s.replace("xmaxi",str(x+w))
			s = s.replace("ymaxi",str(y+w))
			f = open(directory+"/"+"annot/frame"+version+classes+str(count)+".xml", 'w')
			f.write(s)
			print("totalp =",totalp)
			f.close()
			totalp = totalp + 1

		

		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
	count = count+1

	# show the output frame
	
	

	
	# print(count)
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(20) & 0xFF

	# if the 's' key is selected, we are going to "select" a bounding
	# box to track
	if key == ord("s"):
		# select the bounding box of the object we want to track (make
		# sure you press ENTER or SPACE after selecting the ROI)
		box = cv2.selectROI("Frame", frame, fromCenter=False,
			showCrosshair=True)
		
		tracker = OPENCV_OBJECT_TRACKERS[args["tracker"]]()
		trackers.add(tracker, frame, box)


	# if the `q` key was pressed, break from the loop
	elif key == ord("q"):
		print("totalp =",totalp)
		break

# if we are using a webcam, release the pointer
if not args.get("video", False):
	vs.stop()

# otherwise, release the file pointer
else:
	vs.release()

# close all windows
cv2.destroyAllWindows()