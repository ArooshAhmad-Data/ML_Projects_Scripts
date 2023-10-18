import math
import os
import shutil
import json
from random import random

import numpy as np
from PIL import Image, ImageOps


def create_image_dataset(src,dest,no_files_from_src,copy_json: bool, combined_json_file_path):
    combined_json = dict()
    src_files = os.listdir(src)
    selected = random.sample(src_files,no_files_from_src)
    for image in selected:
        new_image_path = os.path.join(src,image)
        if not os.path.exists(dest):
            os.makedirs(dest)
        shutil.copy(new_image_path,dest)

def create_combined_json(src_dirs_list,image_dirs_list,combined_json_file_path):
    combined_json = dict()
    if(len(src_dirs_list) !=  len(image_dirs_list)):
        return "The src and destinations directories must be equal"

    src_files = os.listdir(src_dirs_list)

    for i in range(len(os.listdir(src_dirs_list))):
        """
            The user should have json files in a Json dir
            in each image folder,
            e.g, if image foler is  MyImages/Pattern1, then Json files for the images in Pattern1
            should be in the folder MyImages/Pattger1/Json.
        """

        json_file_path = os.path.join(src_dirs_list[i], "Json/" + src_files[0].split(".")[0] + ".jpg.json")
        if (os.path.exists(json_file_path) and os.path.isfile(json_file_path)):
            with open(json_file_path, 'r') as f:
                data = json.load(f)
                key = str(data["asset"]["id"])
                combined_json[key] = data

    """
        Combined file for json will be a json file with json of all files that we create
        e.g, DmProcessing+export.json, with a key for each image and the key will contain all the
        information for that image.
    """

    with open(combined_json_file_path, 'a') as f:
        f.write(str({"assets": combined_json}))


def rotate_image_qr(img : str ,coords : dict ,rotation_angle : int):
    """
        img : the path of the image
        coords :  coordinates of the qr code location in the image, can be multiple
        rotation_angle: angle by which we need to rotate the portion of image containing
                        the qr code
    """
    image = Image.open(img)
    for i in range(len(coords["X1"])):
        x1 = coords["X1"][i]
        y1 = coords["Y1"][i]
        x2 = coords["X2"][i]
        y2 = coords["Y2"][i]

        box = (x1,y1,x2,y2)
        h,w = (y2-y1,x2-x1)
        qr = image.crop(box)

        # rotate the image by 45 degrees
        rotated_qr = qr.rotate(rotation_angle, expand=True,fillcolor='#414141')

        resized_qr = rotated_qr.resize((w,h))
        image.paste(resized_qr,box)

    return image

