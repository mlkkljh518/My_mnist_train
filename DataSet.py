from PIL import Image
import torch
from torchvision import transforms
from torch.utils.data import DataLoader


class MyDataset(torch.utils.data.Dataset):  # 创建自己的类：MyDataset,这个类是继承的torch.utils.data.Dataset
    def __init__(self, root, datatxt, transform=None, target_transform=None):  # 初始化一些需要传入的参数
        super(MyDataset, self).__init__()
        fh = open(root + datatxt, 'r')  # 按照传入的路径和txt文本参数，打开这个文本，并读取内容
        #print("fh=",fh)
        imgs = []  # 创建一个名为img的空列表，一会儿用来装东西
        for line in fh:  # 按行循环txt文本中的内容
            line = line.rstrip()   # 删除 本行string 字符串末尾的指定字符，这个方法的详细介绍自己查询python
            words = line.split()  # 通过指定分隔符对字符串进行切片，默认为所有的空字符，包括空格、换行、制表符等
            #print("words=",words)
            imgs.append((words[0], int(words[1])))  # 把txt里的内容读入imgs列表保存，具体是words几要看txt内容而定

         # 很显然，根据我刚才截图所示txt的内容，words[0]是图片信息，words[1]是lable
        self.imgs = imgs
        self.transform = transform
        self.target_transform = target_transform

    # 这个方法是必须要有的，用于按照索引读取每个元素的具体内容
    def __getitem__(self, index):
        fn, label = self.imgs[index]  # fn是图片path #fn和label分别获得imgs[index]也即是刚才每行中word[0]和word[1]的信息
        #print("root+fn",root+fn)
        #print("label",label)
        #img = Image.open(root + fn)#.convert('RGB')  # 按照path读入图片from PIL import Image # 按照路径读取图片
        img = Image.open(test_root + fn)  # .convert('RGB')  # 按照path读入图片from PIL import Image # 按照路径读取图片
        #img.show()
        if self.transform is not None:
            img = self.transform(img)  # 是否进行transform
        #print(img)
        return img, label # return很关键，return回哪些内容，那么我们在训练时循环读取每个batch时，就能获得哪些内容

    def __len__(self):  # 这个函数也必须要写，它返回的是数据集的长度，也就是多少张图片，要和loader的长度作区分
        return len(self.imgs)


root="./data/train_data/0_9/"
test_root="./data/test_data/0_9/"
# 根据自己定义的那个勒MyDataset来创建数据集！注意是数据集！而不是loader迭代器
#

