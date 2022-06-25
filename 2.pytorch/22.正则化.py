'''
L1-regularization

regularization_loss=0
for param in model.parameters():
    regularization_loss += torch.sum(torch.abs(param))  1范数：绝对值累加

classify_loss = criteon(logist,target)
loss = classify_loss + 0.01 * regularization_loss

optimizer.zero_grad()
loss.backward()
optimizer.step()


L2-regularization

device = torch.device('cuda:0')
net = MLP().to(device)
optimizer = optim.SGD(net.parameters(),lr = learning_rate,weight_decay = 0.01)
criteon = nn.CrossEntropyLoss().to(device)
'''