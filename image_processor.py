import cv2
import os

# Test print statement
print("This is a test print statement to check if prints are working.")

# Get the desktop path
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# Construct the full path to the image
image_path = os.path.join(desktop_path, 'image.jpg')

# Read the image
image = cv2.imread(image_path)

# Get dimensions of the original image
original_height, original_width = image.shape[:2]
print(f'Original image dimensions: {original_width}x{original_height}')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Get dimensions of the grayscale image
gray_height, gray_width = gray_image.shape[:2]
print(f'Grayscale image dimensions: {gray_width}x{gray_height}')

# Construct the full path to save the grayscale image
gray_image_path = os.path.join(desktop_path, 'grayscale_image.jpg')

# Save the grayscale image
cv2.imwrite(gray_image_path, gray_image)

# Resize the image to 100x100 pixels
resized_image = cv2.resize(image, (100, 100))

# Get dimensions of the resized image
resized_height, resized_width = resized_image.shape[:2]
print(f'Resized image dimensions: {resized_width}x{resized_height}')

# Construct the full path to save the resized image
resized_image_path = os.path.join(desktop_path, 'resized_sample.jpg')

# Save the resized image
if cv2.imwrite(resized_image_path, resized_image):
    print(f'Resized image saved successfully at: {resized_image_path}')
else:
    print('Failed to save resized image.')

# Apply Gaussian blur to the image
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# Construct the full path to save the blurred image
blurred_image_path = os.path.join(desktop_path, 'blurred_sample.jpg')

# Save the blurred image
if cv2.imwrite(blurred_image_path, blurred_image):
    print(f'Blurred image saved successfully at: {blurred_image_path}')
else:
    print('Failed to save blurred image.')
