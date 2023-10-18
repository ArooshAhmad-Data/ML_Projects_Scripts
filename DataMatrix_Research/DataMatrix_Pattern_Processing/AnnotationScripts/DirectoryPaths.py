# For Main Image Folders
# These paths are for creating noised Images from main Images Folder into it as new directory Noised

main_img_dir = ["P1_Renamed_DMs/P1_Renamed_DMs/",
               "P1_Renamed_DMs/P1_Renamed_DMs/horizontal/",
               "P1_Renamed_DMs/P1_Renamed_DMs/vertical/",
                "P1_Renamed_DMs/P1_Renamed_DMs/",
               "P2_Renamed_DMs/P2_Renamed_DMs/horizontal/",
               "P2_Renamed_DMs/P2_Renamed_DMs/vertical/",
                "P3_Renamed_DMs/P3_Renamed_DMs/",
               "P3_Renamed_DMs/P3_Renamed_DMs/horizontal/",
               "P3_Renamed_DMs/P3_Renamed_DMs/vertical/",
                "P4_Renamed_DMs/P4_Renamed_DMs/",
               "P4_Renamed_DMs/P4_Renamed_DMs/horizontal/",
               "P4_Renamed_DMs/P4_Renamed_DMs/vertical/"
              ]

rotated_images_dir= [
    "P1_Renamed_DMs/P1_Renamed_DMs/Rotated/",
    "P1_Renamed_DMs/P1_Renamed_DMs/horizontal/Rotated/",
    "P1_Renamed_DMs/P1_Renamed_DMs/vertical/Rotated/",
    "P2_Renamed_DMs/P2_Renamed_DMs/Rotated/",
    "P2_Renamed_DMs/P2_Renamed_DMs/horizontal/Rotated/",
    "P2_Renamed_DMs/P2_Renamed_DMs/vertical/Rotated/",
    "P2_Renamed_DMs/P2_Renamed_DMs/Rotated/",
    "P2_Renamed_DMs/P2_Renamed_DMs/horizontal/Rotated/",
    "P2_Renamed_DMs/P2_Renamed_DMs/vertical/Rotated/",
    "P2_Renamed_DMs/P2_Renamed_DMs/Rotated/",
    "P2_Renamed_DMs/P2_Renamed_DMs/horizontal/Rotated/",
    "P2_Renamed_DMs/P2_Renamed_DMs/vertical/Rotated/"
]

main_img_noise_dest_dir = [
                "P1_Renamed_DMs/P1_Renamed_DMs/Noised/",
               "P1_Renamed_DMs/P1_Renamed_DMs/horizontal/Noised/",
               "P1_Renamed_DMs/P1_Renamed_DMs/vertical/Noised/",
                "P2_Renamed_DMs/P2_Renamed_DMs/Noised/",
               "P2_Renamed_DMs/P2_Renamed_DMs/horizontal/Noised/",
               "P2_Renamed_DMs/P2_Renamed_DMs/vertical/Noised/",
                "P2_Renamed_DMs/P2_Renamed_DMs/Noised/",
               "P2_Renamed_DMs/P2_Renamed_DMs/horizontal/Noised/",
               "P2_Renamed_DMs/P2_Renamed_DMs/vertical/Noised/",
                "P2_Renamed_DMs/P2_Renamed_DMs/Noised/",
               "P2_Renamed_DMs/P2_Renamed_DMs/horizontal/Noised/",
               "P2_Renamed_DMs/P2_Renamed_DMs/vertical/Noised/"
]

"""
    These directories will now contain the paths for 
    Creating a New Dataset with some images (like, I created for 480 images
    randomly selecting 30 images form each folder) as MyDataset.
"""
new_dataset_img_dirs = [
               "MyDataSet/P1_Renamed_DMs/Noised/Rotated/",
               "MyDataSet/P1_Renamed_DMs/horizontal/Noised/Rotated/",
               "MyDataSet/P1_Renamed_DMs/vertical/Noised/Rotated/",
                "MyDataSet/P2_Renamed_DMs/Noised/Rotated/",
               "MyDataSet/P2_Renamed_DMs/horizontal/Noised/Rotated/",
               "MyDataSet/P2_Renamed_DMs/vertical/Noised/Rotated/",
                "MyDataSet/P3_Renamed_DMs/Noised/Rotated/",
               "MyDataSet/P3_Renamed_DMs/horizontal/Noised/Rotated/",
               "MyDataSet/P3_Renamed_DMs/vertical/Noised/Rotated/",
                "MyDataSet/P4_Renamed_DMs/Noised/Rotated/",
               "MyDataSet/P4_Renamed_DMs/horizontal/Noised/Rotated/",
               "MyDataSet/P4_Renamed_DMs/vertical/Noised/Rotated/"
]


new_dataset_img_dirs_with_rotated = [
                "MyDataSet/P1_Renamed_DMs/Noised/",
                "MyDataSet/P1_Renamed_DMs/Rotated/",
               "MyDataSet/P1_Renamed_DMs/horizontal/Noised/",
               "MyDataSet/P1_Renamed_DMs/horizontal/Rotated/",
               "MyDataSet/P1_Renamed_DMs/vertical/Noised/",
               "MyDataSet/P1_Renamed_DMs/vertical/Rotated/",
                "MyDataSet/P2_Renamed_DMs/Noised/",
                "MyDataSet/P2_Renamed_DMs/Rotated/",
               "MyDataSet/P2_Renamed_DMs/horizontal/Noised/",
               "MyDataSet/P2_Renamed_DMs/horizontal/Rotated/",
               "MyDataSet/P2_Renamed_DMs/vertical/Noised/",
               "MyDataSet/P2_Renamed_DMs/vertical/Rotated/",
                "MyDataSet/P3_Renamed_DMs/Noised/",
                "MyDataSet/P3_Renamed_DMs/Rotated/",
               "MyDataSet/P3_Renamed_DMs/horizontal/Noised/",
               "MyDataSet/P3_Renamed_DMs/horizontal/Rotated/",
               "MyDataSet/P3_Renamed_DMs/vertical/Noised/",
               "MyDataSet/P3_Renamed_DMs/vertical/Rotated/",
                "MyDataSet/P4_Renamed_DMs/Noised/",
                "MyDataSet/P4_Renamed_DMs/Rotated/",
               "MyDataSet/P4_Renamed_DMs/horizontal/Noised/",
               "MyDataSet/P4_Renamed_DMs/horizontal/Rotated/",
               "MyDataSet/P4_Renamed_DMs/vertical/Noised/",
               "MyDataSet/P4_Renamed_DMs/vertical/Rotated/"
              ]

new_dataset_dest_json_dirs = [
               "MyDataSet/P1_Renamed_DMs/Noised/Json/",
               "MyDataSet/P1_Renamed_DMs/Noised/Rotated/Json/",
               "MyDataSet/P1_Renamed_DMs/horizontal/Noised/Json/",
               "MyDataSet/P1_Renamed_DMs/horizontal/Noised/Rotated/Json/",
               "MyDataSet/P1_Renamed_DMs/vertical/Noised/Json/",
               "MyDataSet/P1_Renamed_DMs/vertical/Noised/Rotated/Json/",
               "MyDataSet/P2_Renamed_DMs/Noised/Json/",
               "MyDataSet/P2_Renamed_DMs/Noised/Rotated/Json/",
               "MyDataSet/P2_Renamed_DMs/horizontal/Noised/Json/",
               "MyDataSet/P2_Renamed_DMs/horizontal/Noised/Rotated/Json/",
               "MyDataSet/P2_Renamed_DMs/vertical/Noised/Json/",
               "MyDataSet/P2_Renamed_DMs/vertical/Noised/Rotated/Json/",
               "MyDataSet/P3_Renamed_DMs/Noised/Json/",
               "MyDataSet/P3_Renamed_DMs/Noised/Rotated/Json/",
               "MyDataSet/P3_Renamed_DMs/horizontal/Noised/Json/",
               "MyDataSet/P3_Renamed_DMs/horizontal/Noised/Rotated/Json/",
               "MyDataSet/P3_Renamed_DMs/vertical/Noised/Json/",
               "MyDataSet/P3_Renamed_DMs/vertical/Noised/Rotated/Json/",
               "MyDataSet/P4_Renamed_DMs/Noised/Json/",
               "MyDataSet/P4_Renamed_DMs/Noised/Rotated/Json/",
               "MyDataSet/P4_Renamed_DMs/horizontal/Noised/Json/",
               "MyDataSet/P4_Renamed_DMs/horizontal/Noised/Rotated/Json/",
               "MyDataSet/P4_Renamed_DMs/vertical/Noised/Json/",
               "MyDataSet/P4_Renamed_DMs/vertical/Noised/Rotated/Json/"
              ]


"""
    Contains coordinates of top-left and bottom right, for small qr images in a image as qr_coords,
    and newly added noise squares in the iamges as noise_coords.
"""

import NoiseCoords as nc

noise_coords = [
                nc.noise_coords_pattern1,
                nc.noise_coords_pattern1,
                nc.noise_coords_pattern1,
                nc.noise_coords_pattern2,
                nc.noise_coords_pattern2,
                nc.noise_coords_pattern2,
                nc.noise_coords_pattern3,
                nc.noise_coords_pattern3,
                nc.noise_coords_pattern3,
                nc.noise_coords_pattern4,
                nc.noise_coords_pattern4,
                nc.noise_coords_pattern4
]

qr_coords = [
    "pattern1",
    "pattern1",
    "pattern1",
    "pattern2",
    "pattern2",
    "pattern2",
    "pattern3",
    "pattern3",
    "pattern3",
    "pattern4",
    "pattern4",
    "pattern4"
]


