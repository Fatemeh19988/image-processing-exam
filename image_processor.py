import cv2
import os

# Get the desktop path
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# Construct the full path to the image
image_path = os.path.join(desktop_path, 'image.jpg')

# Read the image
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Construct the full path to save the grayscale image
gray_image_path = os.path.join(desktop_path, 'grayscale_image.jpg')

# Save the grayscale image
cv2.imwrite(gray_image_path, gray_image)
