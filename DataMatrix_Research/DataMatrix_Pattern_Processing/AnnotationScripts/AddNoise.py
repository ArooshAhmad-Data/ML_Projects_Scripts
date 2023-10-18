import cv2
import os

def noise_adder(image_path,coord_array):
    img = cv2.imread(image_path)
    for coord in(coord_array):
        x1,y1,x2,y2 = coord[0],coord[1],coord[2],coord[3],
        cv2.rectangle(img,(x1,y1),(x2,y2),(160, 160, 160),-1)
        cv2.rectangle(img,(x1,y1),(x2,y2),(33, 33, 33),2)
    return img


def create_noised_images(src_path,dest_path,noise_coords):
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    for file in os.listdir(src_path):
        if(file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))):
            img_path = os.path.join(src_path,file)
            noised = noise_adder(img_path,noise_coords)
            new_path = os.path.join(dest_path,file)
            if not os.path.exists(new_path):
                cv2.imwrite(new_path,noised)




