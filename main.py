#at first import the opencv 
import cv2

image=cv2.imread('tomandjerry.png') #get the image by read function

grey_img= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert the image to gray

invert=cv2.bitwise_not(grey_img) #invert the image 

blur=cv2.GaussianBlur(invert,(21,21),0)# blur the image by using gaussianblur function

inverted_blur=cv2.bitwise_not(blur) #Again invert hte blur image

sketch=cv2.divide(grey_img,inverted_blur, scale=256.0)#crete the pencil sketch image

cv2.imwrite('tomandjerrysketch.png',sketch) #get the image as output  by using write function