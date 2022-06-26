# 기존에 있던 클래스 때문에 지정 되어 있던 6,7,10 인덱스를 0,1,2로 각각 변경하기 위한 코드

#!/usr/bin/env python3
import os
import shutil

dir_path = '/home/gigacha/azhes/GRO/green_half'
# dst_path = '/home/gigacha/Downloads/test2'

class0 = int()
class1 = int()
class2 = int()
class3 = int()
class4 = int()
class5 = int()
unknown = int()
cnt = int()

breaker1 = False
breaker2 = False
 
for (root, directories, files) in os.walk(dir_path):
    # print(root, directories, files)
    for file in files:
        if '.txt' in file:
            file_path = os.path.join(root, file)
            # print(file_path)
            a = []
            with open(file_path, "r") as f:
                lines = f.readlines()
                tmp_name = file.replace(".txt", "")
                print(lines)
                for line in lines:
                    class_num = line.split()[0]
                    tmp = line.split()
                    print(tmp)
                    if class_num == '10':
                        tmp[0] = str(int(class_num) - 8)
                        # line_revise = ' '.join(tmp)
                        # a.append(line_revise)
                        # # print(line_revise)
                        # txt = dir_path+ "\\" + tmp_name + '.txt' # (dir_path+tmp_name).split('/')[-1] + '.txt'
                    else:
                        continue
                    # print(type(tmp))
                    # print(tmp)
                    line_revise = ' '.join(tmp)
                    a.append(line_revise)
                    # print(line_revise)
                    txt = dir_path+ "\\" + tmp_name + '.txt' # (dir_path+tmp_name).split('/')[-1] + '.txt'
                print(a)
            with open(file_path, "w") as f2:
                for line in a:
                    f2.write(line + '\n')