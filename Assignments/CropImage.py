# Name:  Jose Ortiz
# Email: jose.ortiz60@myhunter.cuny.edu
# Date:  October 16, 2023
# This program gets an image and crops it

import matplotlib.pyplot as plt
import numpy as np

# Ask the user for the image file name and output file name
image_file = input("Enter image file name: ")
output_file = input("Enter output file: ")

# Read the image using matplotlib
img = plt.imread(image_file)

# Get the height and width of the image
height, width, _ = img.shape

# Crop the lower left quarter of the image
cropped_img = img[height//2:, :width//2, :]

# Save the cropped image to the output file specified by the user
plt.imsave(output_file, cropped_img)

# Display the cropped image
plt.imshow(cropped_img)
plt.show()
