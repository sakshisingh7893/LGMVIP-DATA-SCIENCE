# Name - SAKSHI SINGH

# IMAGE_TO_PENCIL_SKETCH_USING_PYTHON

# BEGINNER LEVEL)

# LEVEL 01



#importing library cv2

import cv2


# reading the picture (jpg format)


original_image = cv2.imread("origianl_pic.jpg")
cv2.imshow("ORIGINAL_IMAGE",original_image)
cv2.waitKey(0)

#forming the gray image of origianl one


gray_image_of_origianl = cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)
cv2.imshow("NEW_IMAGE:",gray_image_of_origianl)
cv2.waitKey(0)

#inverting the gray_image_of_origianl



inverted_image_of_gray_image = 255 - gray_image_of_origianl
cv2.imshow("INVERTED_IMAGE:",inverted_image_of_gray_image)
cv2.waitKey(0)

#converting the inverted_image_of_origianl to blurred one


 blurred_of_gray_image = cv2.GaussianBlur(inverted_image_of_gray_image,(21,21),0)



#dividing the gray_image_of_original with inverted_blurred image to get pencil_sketch look of colourful image

inverted_blurred_image = 255 - blurred_of_gray_image
pencil_sketch_of_origainl = cv2.divide(gray_image_of_origianl,inverted_blurred_image,scale=256)
cv2.imshow("IMAGE_PENCIL_SKETCH:",pencil_sketch_of_origainl)
cv2.waitKey(0)

# code for original(colourful) view and pencil sketch of image


cv2.imshow("ORIGINAL_IMAGE_COLOURFUL:",original_image)
cv2.imshow("PENCIL_SKETCH:",pencil_sketch_of_origainl)
cv2.waitKey(0)
