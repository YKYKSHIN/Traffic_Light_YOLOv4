## red, orange,green 각 클래스마다 train과 test set을 분리하는 코드

#!/usr/bin/env python3
import os
from glob import glob
import shutil
from matplotlib import image
from sklearn.model_selection import train_test_split


src_dir = "/home/gigacha/azhes/red_half"
dst_dir = "/home/gigacha/azhes/data/"

train_dir = dst_dir + "train"
test_dir = dst_dir + "test"

#getting list of images
img_files = glob(os.path.join("/home/gigacha/azhes/red_half/*.jpg"))
images = [name.replace(".jpg", "") for name in img_files]
# print(len(images))

#split the data
#train : test = 8 : 2
train_names, test_names = train_test_split(images,test_size=0.2, random_state=42, shuffle=True)
# test -> 0.5 test /val

def batch_move_files(file_list, src_path, dst_path):
    for file in file_list:
        img = file.split('/')[-1] + '.jpg'
        txt = file.split('/')[-1] + '.txt'
        # #print(img)
        # print("copy img ",os.path.join(src_path, img)," to ", dst_path)
        shutil.copy(os.path.join(src_path, img), dst_path)
        shutil.copy(os.path.join(src_path, txt), dst_path)
    return


print("copy train data to ", train_dir)
batch_move_files(train_names, src_dir, train_dir)
print("finish train data")

print("copy train data to ", test_dir)
batch_move_files(test_names, src_dir, test_dir)
print("finish test data")
