##사진의 갯수와 annotation txt 파일의 pair를 갯수를 통해 확인하는 코드.

import glob, os
import shutil

dir_path = '/home/gigacha/azhes/data/train'

txt_cnt = 0
jpg_cnt = 0

for (root, directories, files) in os.walk(dir_path):
    for file in files:
        if '.txt' in file:
            txt_cnt += 1
        elif '.jpg' in file:
            jpg_cnt += 1

for file in os.listdir(dir_path):
    if jpg_cnt < txt_cnt:
        if file.endswith('.txt'):
            label_name = os.path.splitext(file)[0]
            #print(label_name)

            # Corresponding label file name
            image_name = label_name + '.jpg'
            if os.path.isfile(dir_path + '/' + image_name) == False:
                print(" -- DELETE LABEL [Image file not found -- ]")
                print(label_name)
                label_path = dir_path + '/' + label_name + '.txt'
                os.remove(label_path)
    elif jpg_cnt > txt_cnt :    
        if file.endswith('jpg'):
            image_name = os.path.splitext(file)[0]
            #print(image_name)

            # Corresponding label file name
            label_name = image_name + '.txt'
            if os.path.isfile(dir_path + '/' + label_name) == False:
                print(" -- DELETE IMAGE [Label file not found -- ]")
                print(image_name)
                image_path = dir_path + '/' + image_name + '.jpg'
                os.remove(image_path)
    else :
        print("Pair matches!")