import cv2
import sys

img = cv2.imread("murugar images.jpg")  # Replace with your Image
cv2.imshow("Murgar image", img)         # Replace with your Image
cv2.waitKey(0)
cv2.destroyAllWindows()

if img is None:
    print("Image is not readed")
    sys.exit(1)
else:
    print("Image is readed")
    sys.exit(1)
