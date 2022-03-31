import cv2
import os
import numpy as np

if __name__ == '__main__':
    '''Changing the background of the images to pink'''

    # Creating list of names in folder 'images'.
    image_name_list = os.listdir('images')
    # Opening the pink image
    pink_background = cv2.imread('background.png')
    # Resizing the pink image
    pink_background = cv2.resize(pink_background, (1920, 1080))

    # Looping through the image name list
    for image_name in image_name_list:
        # Print the name of the image
        print(image_name)

        # Opening and resizing the image
        image_path = 'images/' + image_name
        image = cv2.imread(image_path)
        image=cv2.resize(image,(1920,1080))

        # Opening and resizing the mask
        mask_path = 'masks/' + image_name
        mask = cv2.imread(mask_path)
        mask=cv2.resize(mask,(1920,1080))

        # Creating and saving the image with the pink background
        new_image = np.where(mask==0, pink_background, image)
        new_image_path = 'images_pink_background/' + image_name
        cv2.imwrite(new_image_path, new_image)