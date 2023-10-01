# import the necessary packages

from imutils import contours
from skimage import measure
import numpy as np
import imutils
import cv2

#----------------------------------------------------------------------------------------------------------

# load the image

img = cv2.imread('led.jpg')
#cv2.imshow("Image", img)
#cv2.waitKey(2000)

#----------------------------------------------------------------------------------------------------------

# convert it to grayscale, and blur it

grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurimg = cv2.GaussianBlur(grayimg, (3, 3), sigmaX=0, sigmaY=0)

#cv2.imshow("Blurred Image", blurimg)
#cv2.waitKey(2000)

#-----------------------------------------------------------------------------------------------------------

# threshold the image to reveal light regions in the blurred image

_, thresholdimg = cv2.threshold(blurimg, 120, 255, cv2.THRESH_BINARY)

#cv2.imshow("th1", thresholdimg)
#cv2.waitKey(2000)

#------------------------------------------------------------------------------------------------------------

# perform a series of erosions and dilations to remove any small blobs of noise from the thresholded image

kernel = np.ones((3, 3), np.uint8)
erosionimg = cv2.erode(thresholdimg, kernel, iterations=2)

#cv2.imshow("Eroded Image", erosion)
#cv2.waitKey(2000)

dilationimg = cv2.dilate(erosionimg, kernel, iterations=2)

#cv2.imshow("Eroded + Dilated Image", dilation)
#cv2.waitKey(2000)

#--------------------------------------------------------------------------------------------------------------

# perform a connected component analysis on the thresholded image, then initialize a mask to store only the "large" components

nos_Labels, label_id, val, centroid = cv2.connectedComponentsWithStats(thresholdimg, 4, cv2.CV_32S)

#---------------------------------------------------------------------------------------------------------------

# loop over the unique components

output = np.zeros_like(grayimg, dtype="uint8")
#output = np.zeros_like(image_gray)

for i in range(1, nos_Labels):
    area = val[i, cv2.CC_STAT_AREA]

    # if this is the background label (i.e., the largest component), ignore it
    if area > 600:
        continue

    # otherwise, construct the label mask
    lableMask = (label_id == i).astype("uint8") * 255

    # Calculate the number of pixels in the component
    number_pixels = np.sum(lableMask) / 255
    #print(number_pixels,end=" ")

    # if the number of pixels in the component is sufficiently large, then add it to our mask of "large blobs"

    if area>140 and area< 600:  
        large_blobs_mask = cv2.bitwise_or(output, lableMask)

#---------------------------------------------------------------------------------------------------------------

# find the contours in the mask, then sort them from left to right

contours = cv2.findContours(dilationimg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

contours = sorted(contours, key=lambda c: cv2.boundingRect(c)[0])

#----------------------------------------------------------------------------------------------

# Initialize lists to store centroid coordinates and area

centroid_list = []
area_list = []

#----------------------------------------------------------------------------------------------

# Loop over the contours
for cont in contours:
    # Calculate the area of the contour
    area = cv2.contourArea(cont)
    #print (area)
    if area > 1000:
        continue

    # Draw the bright spot on the image
    contour_image = cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
    #cv2.imshow('Contours', contour_image)
    #cv2.waitKey(2000)
    
    # Calculate the centroid coordinates
    M = cv2.moments(cont)
    if M['m00'] != 0:
        cx = float(M['m10'] / M['m00'])
        cy = float(M['m01'] / M['m00'])
    else:
        # Handle the case when the area (m00) is zero to avoid division by zero
        cx, cy = 0, 0

    # Append centroid coordinates and area to the respective lists
    area_list.append(area)
    centroid_list.append((cx , cy))

#------------------------------------------------------------------------------------------------

# Save the output image as a PNG file
cv2.imwrite("led_detection_results.png", img)

# Open a text file for writing
with open("led_detection_results.txt", "w") as file:
    # Write the number of LEDs detected to the file
    file.write(f"No. of LEDs detected: {len(centroid_list)}\n")

    # Loop over the contours
    for i in range (0,len(centroid_list)):
        # Write centroid coordinates and area for each LED to the file
        file.write(f"Centroid #{i + 1}: {centroid_list[i]}\nArea #{i + 1}: {area_list[i]}\n")
# Close the text file
file.close()
