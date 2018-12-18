import cv2
import numpy
from blend_modes import blend_modes
from PIL import Image


import cv2
import numpy as np
 
def dodge(image, mask):
  return cv2.divide(image, 255-mask, scale=256)

def burn(image, mask):
  return 255 - cv2.divide(255-image, 255-mask, scale=256)

img = cv2.imread('cats.jpg', 0)

img2=255-img
blurImg = cv2.GaussianBlur(img2,(7,7),0)
blended=dodge(img,blurImg)




cv2.imshow('image', blended) 
k = cv2.waitKey(0) & 0xFF
  
# wait for ESC key to exit 
if k == 27:  
    cv2.destroyAllWindows() 
      
# wait for 's' key to save and exit 
elif k == ord('s'):  
    cv2.imwrite('messigray.png',img) 
    cv2.destroyAllWindows() 
