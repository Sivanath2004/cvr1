import cv2
import numpy as np

image = cv2.imread('murugar images.jpg')  # Replace with your Image

def adjust_brightness(image, alpha=1.0, beta=50):
    brightened = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return brightened

def apply_blur(image, ksize=(5, 5)):
    blurred = cv2.GaussianBlur(image, ksize, 0)
    return blurred

bright_image = adjust_brightness(image, alpha=1.2, beta=50)
blurred_image = apply_blur(bright_image, ksize=(7, 7))

cv2.imshow('Original Image', image)
cv2.imshow('Brightened Image', bright_image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
