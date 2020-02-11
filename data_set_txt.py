
import sys
from PIL import Image
import matplotlib.image as mpimg
sys.path.append('E:\\Anaconda\\libs')
import os #os：操作系统相关的信息模块
import random #导入随机函数

option_train=False   ## True： 保存 train txt  否则 保存 test  txt
num=3   #0 -2
#存放原始图片地址
data_base_dir = "./data/train_data/"
train_data_all = "./data/train_data/0_9/"
test_data_all = "./data/test_data/0_9/"


if option_train :
    file_list = [] #建立列表，用于保存图片信息

    #读取图片文件，并将图片地址、图片名和标签写到txt文件中
    write_file_name = train_data_all+'train.txt'
    write_file = open(write_file_name, "w") #以只写方式打开write_file_name文件
    for  n in range(num):
        for file in os.listdir(data_base_dir+str(n)+"/"): #file为current_dir当前目录下图片名
            if file.endswith(".png"): #如果file以jpg结尾
                write_name = file.split('.')[0]+'_'+str(n)+'.png' #图片路径 + 图片名 + 标签
                I = Image.open(data_base_dir+str(n)+"/"+file)
                #I.show()
                I.save(train_data_all+write_name)


    # train  data  txt 写入
    for file in os.listdir(train_data_all): #file为current_dir当前目录下图片名
        if file.endswith(".png"): #如果file以jpg结尾
            write_name = file #图片路径 + 图片名 + 标签
            label=(write_name.split('_')[3]).split('.')[0]
            print(write_name)
            print(label)
            file_list.append(write_name+ '  ' + label) #将write_name添加到file_list列表最后
            sorted(file_list) #将列表中所有元素随机排列
    number_of_lines = len(file_list) #列表中元素个数
    #将图片信息写入txt文件中，逐行写入
    for current_line in range(number_of_lines):
        write_file.write(file_list[current_line] + '\n')
    #关闭文件
    write_file.close()
else:


    file_list = []
    write_file_name = test_data_all+'test.txt'
    write_file = open(write_file_name, "w") #以只写方式打开write_file_name文件
    # test txt 写入
    for file in os.listdir(test_data_all): #file为current_dir当前目录下图片名
        if file.endswith(".png"): #如果file以jpg结尾
            write_name = file #图片路径 + 图片名 + 标签
            label=(write_name.split('_')[3]).split('.')[0]
            print(write_name)
            print(label)
            file_list.append(write_name+ '  ' + label) #将write_name添加到file_list列表最后
            sorted(file_list) #将列表中所有元素随机排列
    number_of_lines = len(file_list) #列表中元素个数
    #将图片信息写入txt文件中，逐行写入
    for current_line in range(number_of_lines):
        write_file.write(file_list[current_line] + '\n')
    #关闭文件
    write_file.close()