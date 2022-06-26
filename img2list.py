#Train과 Test set에 있는 파일명을 txt 파일에 리스트로 써주는 코드

import os


#dataset 정합 후 train:test = 8:2 로 data/train data/test 에 저장하고 
#이코드 각 각 돌려서 위에처럼 txt파일 생성해야함 생성된 txt파일들 train돌릴때 넣어줘야함

# dir_path => "<your_directory>/data"
dir_path = "/home/gigacha/azhes/data/test"
train_data_path = "data/train"
test_data_path = "data/test"

data = []
for (root, directories, files) in os.walk(dir_path):
    print(files)
    for file in files:
        if '.jpg' in file:
            #file_path = os.path.join(train_data_path, file)
            file_path = os.path.join(test_data_path, file)
            # print(file_path)
            data.append(file_path)

# train.txt / test.txt 
data_list = open(r'test.txt','w') 

for i in data:
    data_list.write(i + '\n')

data_list.close()