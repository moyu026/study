'''
$Dropout$
Learning less to learn better
Each connection has p = [0,1] to lose

net_dropped = torch.nn.Sequential(
    torch.nn.Linear(784,200),
    torch.nn.Dropout(0.5),      # 加入dropout层，断掉部分链接
    torch.nn.ReLU(),
    torch.nn.Linear(200,200),
    torch.nn.Dropout(0.5),
    torch.nn.ReLU(),
    torch.nnLinear(200,10),
)
'''

'''
$Behavior\space betweenn\space train\space and\space test$
训练的时候加入dropout层，测试的时候去掉dropout层
for epoch in range(epochs):
    net_dropped.train()
    for batch_idx,(data,target) in enumerate(train_loader):
        ...
        net_dropped.eval()
        test_loss = 0
        correct = 0
        for data,target in test_loader:
            ...
'''