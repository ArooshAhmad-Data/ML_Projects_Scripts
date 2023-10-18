from PIL import Image
import os


def create_horizontal_flipping(image_dir,dest_dir):
    # Loop through each file in the directory
    for filename in os.listdir(image_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Open the image file
            image = Image.open(os.path.join(image_dir, filename))

            # Flip the image horizontally
            flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)

            # Save the flipped image with a new filename
            flipped_image.save(os.path.join(dest_dir, filename + '_horizontal'))

def create_vertical_flipping(image_dir,dest_dir):
    # Loop through each file in the directory
    for filename in os.listdir(image_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Open the image file
            image = Image.open(os.path.join(image_dir, filename))

            # Flip the image vertically
            flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)

            # Save the flipped image with a new filename
            flipped_image.save(os.path.join(dest_dir, filename + '_vertical'))


