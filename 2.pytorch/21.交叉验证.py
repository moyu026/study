import torch
import torch.nn as nn
import torchvision
from torchvision import datasets,transforms
from torch.nn import functional as F
import torch.optim as optim

batch_size = 200
learning_rate  = 1e-2
epochs = 10

'''train_db和test_db是torch原生提供的两种划分'''
train_db =  datasets.MNIST('datasets/mnist_data',
                train=True,
                download=True,
                transform=torchvision.transforms.Compose([
                torchvision.transforms.ToTensor(),                       # 数据类型转化
                torchvision.transforms.Normalize((0.1307, ), (0.3081, )) # 数据归一化处理
    ]))

train_loader = torch.utils.data.DataLoader(
        train_db,
        batch_size = batch_size,
        shuffle = True)

test_db = datasets.MNIST('datasets/mnist_data/',
                train=False,
                download=True,
                transform=torchvision.transforms.Compose([
                torchvision.transforms.ToTensor(),
                torchvision.transforms.Normalize((0.1307, ), (0.3081, ))
    ]))

test_loader = torch.utils.data.DataLoader(
        test_db,
        batch_size = batch_size,
        shuffle = True
)


print('train:', len(train_db), 'test:', len(test_db))
'''把得到的60k训练样本重新划分成50k训练集和10k验证集'''
train_db, val_db = torch.utils.data.random_split(train_db, [50000, 10000])
print('db1:', len(train_db), 'db2:', len(val_db))
train_loader = torch.utils.data.DataLoader(
    train_db,
    batch_size=batch_size, shuffle=True)
val_loader = torch.utils.data.DataLoader(
    val_db,
    batch_size=batch_size, shuffle=True)

class MLP(nn.Module):

    def __init__(self):
        super(MLP, self).__init__()

        self.model = nn.Sequential(
            nn.Linear(784, 200),
            nn.LeakyReLU(inplace=True),
            nn.Linear(200, 200),
            nn.LeakyReLU(inplace=True),
            nn.Linear(200, 10),
            nn.LeakyReLU(inplace=True),
        )

    def forward(self, x):
        x = self.model(x)

        return x

device = torch.device('cuda:0')
net = MLP().to(device)
optimizer = optim.SGD(net.parameters(), lr=learning_rate)
criteon = nn.CrossEntropyLoss().to(device)

for epoch in range(epochs):

    for batch_idx, (data, target) in enumerate(train_loader):
        data = data.view(-1, 28*28)
        data, target = data.to(device), target.cuda()

        logits = net(data)
        loss = criteon(logits, target)

        optimizer.zero_grad()
        loss.backward()
        # print(w1.grad.norm(), w2.grad.norm())
        optimizer.step()

        if batch_idx % 100 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                       100. * batch_idx / len(train_loader), loss.item()))

# 每一段数据过拟合时把这一段最好的训练参数保存下来
    test_loss = 0
    correct = 0
    for data, target in val_loader:
        data = data.view(-1, 28 * 28)
        data, target = data.to(device), target.cuda()
        logits = net(data)
        test_loss += criteon(logits, target).item()

        pred = logits.data.max(1)[1]
        correct += pred.eq(target.data).sum()

    test_loss /= len(val_loader.dataset)
    print('\nVAL set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(val_loader.dataset),
        100. * correct / len(val_loader.dataset)))



test_loss = 0
correct = 0
for data, target in test_loader:
    data = data.view(-1, 28 * 28)
    data, target = data.to(device), target.cuda()
    logits = net(data)
    test_loss += criteon(logits, target).item()

    pred = logits.data.max(1)[1]
    correct += pred.eq(target.data).sum()

test_loss /= len(test_loader.dataset)
print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
    test_loss, correct, len(test_loader.dataset),
    100. * correct / len(test_loader.dataset)))