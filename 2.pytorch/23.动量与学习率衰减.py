'''
动量 momentum

optimizer = torch.optim.SGD(model.parameters().args.lr,
                               momentum = args.momentum,            #动量
                               weight_decay = args.weight_decay)    #L2正则化
scheduler = ReduceLOonPlateau(optimizer,'min')
for epoch in xrange(args.start_epoch,args.epochs):
    train(train_loader,model,criterion,optimizer,epoch)
    result_avg,loss_val = validate(val_loader,model,criterion,epoch)
    scheduler.step(loss_val)

'''

'''
学习率 learning_rate

(1)optimizer = torch.optim.SGD(model.parameters().args.lr,
                               momentum = args.momentum,
                               weight_decay = args.weight_decay)
scheduler = ReduceLOonPlateau(optimizer,'min')
for epoch in xrange(args.start_epoch,args.epochs):
    train(train_loader,model,criterion,optimizer,epoch)
    result_avg,loss_val = validate(val_loader,model,criterion,epoch)
    scheduler.step(loss_val)
    
(2)scheduler = StepLR(optimizer,step_size = 30,gamma = 0.1)
for epoch in range(100):
    scheduler.step()
    train(...)
    validate(...)
'''