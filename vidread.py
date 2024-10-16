import cv2 # OpenCV library used for image/video processing
  
def FrameCapture(path): # Function to extract frames 
     
    vidObj = cv2.VideoCapture(path) # Path to video file
    
    count = 0 # Used as counter variable 
    success = 1 # Checks whether frames were extracted 
  
    while success: 

        success, image = vidObj.read() # vidObj object calls read function to extract frames 
        cv2.imwrite("D:\\Frames\\frame%d.jpg" % count, image) # Saves the frames with frame-count
        count += 1
   
if __name__ == '__main__': 

    FrameCapture("D:\\52-24 stretching oct-31.mp4") # Path to the video on my laptop