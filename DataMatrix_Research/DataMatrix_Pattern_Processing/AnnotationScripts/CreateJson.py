import os
import json
import cv2
import random
import string

import NoiseCoords as nc
import PatternCoords as pc
import FormatsForAnnotation as fa

coord_noise = nc.noise_coords_pattern1
coord_qr = pc.Patterns["pattern1"]
length = 32

def create_combined_json(base_path,json_dir_paths,dest_file_path):
    """
        base_path : base path of the direcotory on local machine
        json_dir :  path of the json directory containing the separate jsons for wach image
        dest_file_path: file path of the combined json file
        Takes path of the directory containing the images and their associated json files
        and then combine all the json files and dump into a single destination json file.
    """
    merged_data = {"assets":{}}
    for i in range(len(json_dir_paths)):
        dir_path =os.path.join(base_path,json_dir_paths[i])
        files = os.listdir(dir_path)
        for file in files:
            file_path = os.path.join(dir_path,file)
            with open(file_path,'r') as f :
                data = json.load(f)
                merged_data["assets"][data["asset"]["id"]] = data

    with open(dest_file_path,'a') as file:
        json.dump(merged_data,file)





def  create_json(base_path,dst_path,pattern,coords):
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)
    for file in os.listdir(base_path):
        if(file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))):
            img = cv2.imread(os.path.join(base_path,file))
            basic = fa.Basic_Format
            basic["asset"]["name"] = file
            basic["asset"]["id"] = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))
            basic["asset"]["path"] = str(os.path.join(base_path,file))
            height,width = img.shape[:2]
            basic["asset"]["size"]["width"] = width
            basic["asset"]["size"]["height"] = height
            new_regions = create_regions(pattern,coords)
            basic["regions"] = new_regions
            json_file = json.dumps(basic)
            file_path = dst_path+"/"+str(file)+".json"
            if not os.path.exists(file_path):
                with open(file_path, 'w') as f:
                    f.write(json_file)
                    f.close()



def create_regions(pattern,pattern_coords):
    length = 8
    regions = []
    for i in range(len(pc.Patterns[pattern]["X1"])):
        x1 = pc.Patterns[pattern]["X1"][i]
        y1 = pc.Patterns[pattern]["Y1"][i]
        x2 = pc.Patterns[pattern]["X2"][i]
        y2 = pc.Patterns[pattern]["Y2"][i]
        dm_region = {"id":"","boundingBox":{"height":"","width":"","left":"","top":""},"points":{}}
        dm_region["id"] = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length))
        dm_region["tags"] = ["DM"]
        dm_region["boundingBox"]["height"] = abs(y2-y1)
        dm_region["boundingBox"]["width"] = abs(x2-x1)
        dm_region["boundingBox"]["left"] = x1
        dm_region["boundingBox"]["top"] = y1
        point = points_generator(x1,y1,x2,y2)
        dm_region["points"] = point
        region = dm_region
        regions.insert(i,region)

    for i in range(len(pattern_coords)):
        x1 = pattern_coords[i][0]
        y1 = pattern_coords[i][1]
        x2 = pattern_coords[i][2]
        y2 = pattern_coords[i][3]
        nodm_region = {"id":"","boundingBox":{"height":"","width":"","left":"","top":""},"points":{}}
        nodm_region["id"] = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length))
        nodm_region["boundingBox"]["height"] = abs(y2-y1)
        nodm_region["boundingBox"]["width"] = abs(x2-x1)
        nodm_region["boundingBox"]["left"] = x1
        nodm_region["boundingBox"]["top"] = y1
        nodm_region["tags"]=["NoDM"]
        point = points_generator(x1, y1, x2, y2)
        nodm_region["points"] = point
        region = nodm_region
        regions.append(region)

    return regions

def points_generator(x1,y1,x2,y2):
    points = []

    point1 = {"X": 0, "Y": 0}
    point1["X"] = x1
    point1["Y"] = y1

    point2 = {"X": 0, "Y": 0}
    point2["X"] = x2
    point2["Y"] = y1

    point3 = {"X": 0, "Y": 0}
    point3["X"] = x1
    point3["Y"] = y2

    point4 = {"X": 0, "Y": 0}
    point4["X"] = x2
    point4["Y"] = y2

    points.append(point1)
    points.append(point2)
    points.append(point3)
    points.append(point4)

    return  points


