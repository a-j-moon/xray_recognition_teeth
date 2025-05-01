import pathlib

import numpy as np
import matplotlib.pyplot as plt


# Setup paths to data
data_dir = pathlib.Path('Data', 'Dental-periapuical-x-ray-dataset')
img_dir = data_dir / 'Images'
annotations_dir = data_dir / 'Annotations'

# Cavities are (246,51,81) color in annotation. Divide by 255 to
# convert to between 0 and 1
cav_col = np.array((246, 51, 81)).astype(np.int16)

cav_imgs = []
no_cav_imgs = []
n = 0
for annotation_file in annotations_dir.iterdir():
    # Print progress bar
    if annotation_file.suffix.lower() != '.png':
        # Go right back to the start of the loop, skip this file
        # since it's not a JPG image
        continue

    # Load the image in as an array of its pixels
    ann_img_array = plt.imread(annotation_file)

    # Reshape array to array of pixels represented by an array of 3
    # values: RGB
    pixel_array = ann_img_array.reshape(-1, 3)
    # Scale to between 0-255
    pixel_array = pixel_array * (255, 255, 255)
    # Convert to integer
    pixel_array = pixel_array.astype(np.int16)

    # Check for cavity-colored pixel
    if np.any(pixel_array == cav_col):
        cav_imgs.append(annotation_file.name + '\n')
    else:
        no_cav_imgs.append(annotation_file.name + '\n')

    # Increment the counter indicating how many images we've checked
    n += 1

# Write all the cavity image file names to a txt file
with open('cav_files.txt', 'w') as file:
    file.writelines(cav_imgs)

# Write all the no-cavity image file names to a txt file
with open('no_cav_files.txt', 'w') as file:
    file.writelines(no_cav_imgs)
