import os
import cv2
import shutil

import numpy as np

from CreateJson import create_json, create_combined_json
from AddNoise import create_noised_images
from DirectoryPaths import noise_coords,qr_coords, main_img_dir,main_img_noise_dest_dir,new_dataset_img_dirs,new_dataset_dest_json_dirs
from CreateCustomDatasets import rotate_image_qr
from Script.AnnotationScripts.PatternCoords import Patterns


base_path = "C:/Users/17802/Desktop/QR_Project/Script/"


# for i in range(len(qr_coords)):
#     print(noise_coords[i])
#     if os.path.exists((main_img_dir[i])):
#         shutil.rmtree(main_img_noise_dest_dir[i])
#     create_noised_images(main_img_dir[i], main_img_noise_dest_dir[i], noise_coords[i])
#     json_dir = os.path.join(base_path,os.path.join(new_dataset_img_dirs[i],"Json"))
#     main_dir = os.path.join(base_path,new_dataset_img_dirs[i])
#     create_json(main_dir,json_dir,qr_coords[i],noise_coords[i])
#
# rotated_image  = rotate_image_qr(
#     "C:/Users/17802/Desktop/QR_Project/Script/Pattern1/C2X000480_18_P1_10252022_081330_Die1998_x82005u_y36810u.jpg",
#     Patterns["pattern1"],
#     45
# )
#
# cv2.imshow("rotated",np.array(rotated_image))
# cv2.waitKey(0)

# base_path = "C:/Users/17802/Desktop/QR_Project/Script/"
# for i in range(len(new_dataset_img_dirs)):
#     dir = new_dataset_img_dirs[i]
#     ptrn = qr_coords[i]
#     coords = Patterns[ptrn]
#     dir_path = os.path.join(base_path, dir)
#     files_list = os.listdir(dir_path)
#     rotated_dir = os.path.join(dir_path,"Rotated/")
#     if not os.path.exists(rotated_dir):
#         os.makedirs(rotated_dir)
#     for file in files_list:
#         img_path = os.path.join(dir_path,file)
#         if os.path.isfile(img_path) and (file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))):
#             image = rotate_image_qr(img_path,coords,45)
#             image = np.array(image)
#             cv2.imwrite(os.path.join(rotated_dir,file), image)
        # print(img_path)
        # cv2.imwrite(rotated_dir, image)

# create_rotated_image_dataset(main_img_dir,main_img_dir,qr_coords,45)

dest_json_dir = "C:/Users/17802/Desktop/QR_Project/Script/MyDataset/Merged_Dm_Json.json"
base_path = "C:/Users/17802/Desktop/QR_Project/Script/"
create_combined_json(base_path,new_dataset_dest_json_dirs,dest_json_dir)


