#!/usr/bin/env python3
# Description:
# - Subscribes to real-time streaming video from your built-in webcam.
#
# Author:
# - Addison Sears-Collins
# - https://automaticaddison.com
 
# Import the necessary libraries
import rospy # Python library for ROS
from sensor_msgs.msg import Image,CompressedImage # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library
import numpy as np
from ultralytics import YOLO
import torch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
torch.cuda.init()
rospy.loginfo(torch.cuda.is_available())

model_path = '/home/aurora/Downloads/arrow_300.pt'  # Replace with the path to your YOLOv8 model weights
model = YOLO(model_path)
threshold = 0.6
def classify_arrow(arrow_image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(arrow_image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding to get a binary image
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not contours:
        return None, None

    # Find the largest contour
    largest_contour = max(contours, key=cv2.contourArea)

    # Get the centroid of the largest contour
    M = cv2.moments(largest_contour)
    if M["m00"] == 0:
        return None, None
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])

    # Determine the direction of the arrow based on centroid position
    image_center_x = arrow_image.shape[1] // 2
    direction = "left" if cx < image_center_x else "right"

    return direction, largest_contour
def callback(data):
 
  # Used to convert between ROS and OpenCV images
  #br = CvBridge()
 
  # Output debugging information to the terminal
  #rospy.loginfo("receiving video frame")
  br = np.frombuffer(data.data, np.uint8)
  image_np = cv2.imdecode(br, cv2.IMREAD_COLOR)

  results = model(image_np)[0]

  for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
        

        if score > threshold:
            cv2.rectangle(image_np, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            #cv2.putText(image_np, results.names[int(class_id)].upper(), (int(bbox_cx)), int(bbox_cy - 10),
                       # cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            cropped_image = image_np[int(y1):int(y2),int(x1):int(x2)]
            cv2.imshow("croppedFrame", cropped_image)
  # Convert ROS Image message to OpenCV image
  #current_frame = br.imgmsg_to_cv2(data)
  # Display image
  #width = 1280
  #height = 720
  #img = cv2.resize(image_np, (width, height))
  #center = (int(width/2),int(height/2))
  #img = cv2.line(img,(center[0]-100,0),(center[0]-100,height),(0,255,0),1)
  #img = cv2.line(img,(center[0]+100,0),(center[0]+100,height),(0,255,0),1)
  cv2.imshow("Frame", image_np)
  
   
  cv2.waitKey(1)
def receive_message():
 
  # Tells rospy the name of the node.
  # Anonymous = True makes sure the node has a unique name. Random
  # numbers are added to the end of the name. 
  rospy.init_node('video_sub_py', anonymous=True)
   
  # Node is subscribing to the video_frames topic
  rospy.Subscriber('/usb_cam/image_raw/compressed', CompressedImage, callback)
 
  # spin() simply keeps python from exiting until this node is stopped
  rospy.spin()
 
  # Close down the video stream when done
  cv2.destroyAllWindows()
  
if __name__ == '__main__':
  receive_message()
