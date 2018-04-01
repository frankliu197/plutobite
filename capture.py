# needed to capture image
import cv2
# Import the base64 encoding library to encode image
 

def capture(ad_num):
    #Camera 0 = webcam for laptop, this should be changed for USB camera
    camera_port = 0
     
    camera = cv2.VideoCapture(camera_port)#creates camera object using webcam index
     
    def get_image():#gets single image
        retval, im = camera.read()
        return im
	
    camera_capture = get_image()
    file_name = "images/ad" + str(ad_num) + ".jpg" #file path for the given snapShot
    
    cv2.imwrite(file_name, camera_capture)
    del(camera)#deletes camera in order to create another later
    return file_name
