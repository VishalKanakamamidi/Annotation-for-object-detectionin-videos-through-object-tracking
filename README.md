# Annotation-for-object-detection-in-videos-through-object-tracking
Here I have used object tracking through OpenCV to annotate the frames of a video for object detection <br/>
The annotation format is Pascal VOC format <br/>
# Reqirements - <br/>
Python3.6,imutils,opencv-contrib-python <br/>
# To generate annotations and the corresponding frames do the following thing - <br/>
1.python autoannotate.py --video videoname.mp4 --tracker csrt (Run this command if the video is taken from a file) <br/>
2.python autoannotate.py --tracker csrt (Run this command if the video is taken from a webcam) <br/>
3.Enter the class name -(Note - I have designed the code to annotate a single class in a video frame) <br/>
4.Enter the version (Version can be used when you take multiple videos containing same class i.e. v1 for video 1 and v2 for video 2.) <br/>
5.Enter y (Again?) - If you want to create a new class file in items.<br/>
6.Enter n(Again?) - If you already have the class file in items folder and you want to annotate more images related to the class.<br/>
7.Press s to stop the video <br/>
8.Draw the bounding box around the object you want to annotate <br/>
9.Press SPACE bar to continue tracking
10.Press q to quit
# Implementation Video-<br/>
Checkout this video for implementation - https://www.youtube.com/watch?v=mKeT6GFoV-k <br/>
