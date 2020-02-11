import torch

import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from  model import  LeNet
import torch.optim as optim
from DataSet  import  MyDataset
from tensorboardX import SummaryWriter
from torch.utils.data import DataLoader

root="./data/train_data/0_9/"

# 根据自己定义的那个勒MyDataset来创建数据集！注意是数据集！而不是loader迭代器

train_data = MyDataset(root=root, datatxt='train.txt', transform=transforms.ToTensor())


train_loader  = DataLoader(dataset=train_data, batch_size=32, shuffle=True)


net = LeNet()

criterion = nn.CrossEntropyLoss()
optimizer=optim.SGD(net.parameters(),lr=0.001,momentum=0.9)

print("Start Traing ...")
j=0
writer = SummaryWriter('runs')
for epoch in range(80):
    # 我们用一个变量来记录每100个batch的平均loss

    loss100 = 0.0
    for i, data in enumerate(train_loader):
        inputs,labels=data

        optimizer.zero_grad()
        outputs=net(inputs)
        loss = criterion(outputs,labels)
        loss.backward()
        optimizer.step()
        loss100 +=loss.item()
        if i%100 ==99:
            loss_mean_100=loss100/100
            print('[epoch %d,Batch %5d] loss: %.6f' %(epoch + 1,i+1,loss_mean_100))
            loss100 =0.0
            j=j+1
            writer.add_scalar('loss_mean_100', loss_mean_100, global_step=j)

writer.close()
# 2 ways to save the net
torch.save(net, 'net.pkl')  # save entire net
#torch.save(net.state_dict(), 'net_params.pkl')  # save only the parameters

print("Done Training !")






