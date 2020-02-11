# My_mnist_train

训练阶段：
修改DataSet.py 中对应代码如下

    def __getitem__(self, index):
       img = Image.open(root + fn)#.convert('RGB')  # 按照path读入图片from PIL import Image # 按照路径读取图片
 测试阶段：
 修改DataSet.py 中对应代码如下
   def __getitem__(self, index):
     img = Image.open(test_root + fn)  # .convert('RGB')  # 按照path读入图片from PIL import Image # 按照路径读取图片
