from visdom import Visdom

# lines: single trace
viz = Visdom()
''' 创建一个点（[y],[x]）,标识符的名字"train_loss",标题是’train loss‘'''
viz.line([0],[0],win='train_loss',opts=dict(title='train loss'))
'''[loss.item()]:传入的数据；[global_step]:x轴时间戳；update='append：更新曲线上的点'''
viz.line([loss.item()],[global_step],win='train_loss',update='append')

# multi-traces 多条曲线
viz = Visdom()
'''([y1,y2],[x])；legend = ['loss','acc'])；两条曲线的标签'''
viz.line([[0.0,0.0]],[0.],win = 'test',opts = dict(title = 'test loss & acc',
                                   legend = ['loss','acc']))
viz.line([[test_loss,correct / len(test_loader.dataset)]],
         [global_step],win = 'test',update = 'append') # 传入数据

# visual X
viz = Visdom()
viz.images(data.view(-1,1,28,28),win = 'x')
viz.text(str(pred.detach().cpu().numpy()),win = 'pred',opts = dict(title = 'pred'))