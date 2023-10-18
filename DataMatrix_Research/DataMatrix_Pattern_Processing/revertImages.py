from PIL import Image
import numpy as np
import os
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("dirpath")
parser.add_argument("pattern")
args = parser.parse_args()
dir = args.dirpath
pattern = args.pattern

# print(type(dir))
# print(type(pattern))

horizontal_dir = os.path.join(dir,"horizontal")
vertical_dir =  os.path.join(dir,"vertical")

if not os.path.exists(vertical_dir):
    os.mkdir(vertical_dir)

if not os.path.exists(horizontal_dir):
    os.mkdir(horizontal_dir)


# X1 -> Bottom-Left's X
# Y1 -> Top-Right's Y
# X2 -> Top-Right's X
# Y2 -> Bottom-Lext's Y

Patterns = {
    "pattern1" : {
    "X1":[376,646,370,649,369,639,377,644],
    "Y1":[266,236,554,540,850,828,1453,1424],
    "X2":[629,945,635,944,635,955,633,949],
    "Y2":[516,540,817,832,1116,1140,1695,1695]
    },
    "pattern2" : {
    "X1":[658,897,658,888,673,887,139,276,145,280,133,275,684,896],
    "Y1":[319,229,582,561,843,829,767,771,894,904,1015,1024,1506,1486],
    "X2":[881,1136,896,1153,890,1149,271,387,270,389,275,396,887,1137],
    "Y2":[512,537,793,814,1066,1089,893,888,1020,1013,1158,1147,1695,1695]
    },
"pattern3" : {
    "X1":[118,187,252,109,170,252,536,670,532,670,525,663,130,226,346,113,211,339,914,1016,917,1015,906,1007,880,965,1064,874,957,1057,128,359,619,126,347,603,907,1017,907,1016,899,1006,120,185,257,109,170,254,536,674,883,963,1064,875,955,1059],
    "Y1":[244,247,248,306,304,313,261,249,408,396,551,541,436,428,437,536,526,534,486,587,587,589,694,684,251,249,254,329,324,333,775,756,768,1002,980,991,880,874,997,989,1107,1098,1437,1438,1440,1494,1490,1502,1448,1441,1437,1435,1442,1520,1513,1524],
    "X2":[178,239,306,172,243,306,655,812,661,814,659,823,208,327,428,212,327,432,1003,1116,1007,1118,1007,1123,952,1040,1130,957,1049,1134,332,586,811,328,593,827,998,1121,1002,1124,1005,1135,173,240,303,172,242,306,655,811,953,1042,1130,956,1048,1132],
    "Y2":[303,300,302,371,376,367,380,390,531,542,684,697,507,524,517,633,642,631,573,684,682,684,792,801,323,321,319,411,417,409,967,983,964,1203,1225,1214,974,981,1092,1100,1214,1224,1491,1491,1488,1559,1564,1554,1566,1579,1509,1512,1507,1602,1608,1595]
},
    "pattern4" : {
    "X1":[227,640,225,614],
    "Y1":[419,380,855,814],
    "X2":[614,1086,609,1106],
    "Y2":[784,821,1239,1275]
    },

}
pattern1 = {
    "X1":[376,646,370,649,369,639,377,644],
    "Y1":[266,236,554,540,850,828,1453,1424],
    "X2":[629,945,635,944,635,955,633,949],
    "Y2":[516,540,817,832,1116,1140,1695,1695]
}

# print("Dir is  : ",dir)


for file in os.listdir(dir):
    #load the image
    # print("Type of file is :", type(file))
    image_path = os.path.join(dir,file)
    image = Image.open(image_path)

    for i in range(len(Patterns[pattern]["X1"])):
        x1 = Patterns[pattern]["X1"][i]
        y1 = Patterns[pattern]["Y1"][i]
        x2 = Patterns[pattern]["X2"][i]
        y2 = Patterns[pattern]["Y2"][i]
        section = image.crop((x1, y1, x2, y2))
        flipped_section = np.flip(section, axis=1)
        image.paste(Image.fromarray(flipped_section), (x1, y1, x2, y2))
    file_name = file.split(".")[0]+"_horizontal"+".jpg"
    modified_path = os.path.join(horizontal_dir,file_name)
    if not os.path.exists(modified_path):
        image.save(modified_path)
    for i in range(len(Patterns[pattern]["X1"])):
        x1 = Patterns[pattern]["X1"][i]
        y1 = Patterns[pattern]["Y1"][i]
        x2 = Patterns[pattern]["X2"][i]
        y2 = Patterns[pattern]["Y2"][i]
        section = image.crop((x1, y1, x2, y2))
        flipped_section = np.flip(section, axis=0)
        image.paste(Image.fromarray(flipped_section), (x1, y1, x2, y2))
    file_name = file.split(".")[0]+"_vertical"+".jpg"
    modified_path = os.path.join(vertical_dir,file_name)
    if not os.path.exists(modified_path):
        image.save(modified_path)

# python revertImages.py "C:\Users\17802\Desktop\Image Processing\P4_Renamed_DMs\P4_Renamed_DMs" "pattern4"

# # load the image
# image_path = "C2X000480_18_P1_10252022_081330_Die2000_x73405u_y36810u.jpg"
# image = Image.open(image_path)


# for i in range(len(coordinates["X1"])):
#     x1 = coordinates["X1"][i]
#     y1 = coordinates["Y1"][i]
#     x2 = coordinates["X2"][i]
#     y2 = coordinates["Y2"][i]
#     section = image.crop((x1, y1, x2, y2))
#     flipped_section = np.flip(section, axis=1)
#     image.paste(Image.fromarray(flipped_section), (x1, y1, x2, y2))

# # # save the modified image
# modified_image_path = "modified_horizontal.jpg"
# image.save(modified_image_path)


# # extract the section of the image
# section = image.crop((x1, y1, x2, y2))

# # flip the section
# flipped_section = np.flip(section, axis=1)

# cv2.imshow("Showing after flipping",flipped_section)
# cv2.waitKey(0)

# # # paste the flipped section back into the original image
# image.paste(Image.fromarray(flipped_section), (x1, y1, x2, y2))

# # # save the modified image
# modified_image_path = "modified.jpg"
# image.save(modified_image_path)


