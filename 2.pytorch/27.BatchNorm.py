import torch
import torch.nn as nn


# U(0.5,1) 均匀分布
x = torch.rand(100,16,784) # 784=28*28,1维数据
# Channels
layer = nn.BatchNorm1d(16)  # 通道数
out = layer(x)

# print(layer.running_mean)  # 均值在0.05
'''tensor([0.0503, 0.0499, 0.0499, 0.0500, 0.0501, 0.0502, 0.0500, 0.0500, 0.0498,
        0.0499, 0.0501, 0.0500, 0.0503, 0.0501, 0.0500, 0.0500])'''
# print(layer.running_var)   # 方差在1
'''tensor([0.9083, 0.9083, 0.9083, 0.9084, 0.9083, 0.9083, 0.9083, 0.9084, 0.9084,
        0.9084, 0.9083, 0.9084, 0.9083, 0.9084, 0.9083, 0.9083])'''


x = torch.rand(1,16,7,7)
layer = nn.BatchNorm2d(16)
out = layer(x)
# print(layer.weight)   #  对应gama
'''Parameter containing:
tensor([1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
       requires_grad=True)'''
# print(layer.bias)   # 对应beita
'''Parameter containing:
tensor([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       requires_grad=True)'''

print(vars(layer))
'''{'training': True, '_parameters': OrderedDict([('weight', Parameter containing:
tensor([1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
       requires_grad=True)), ('bias', Parameter containing:
tensor([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       requires_grad=True))]), 
       '_buffers': OrderedDict([('running_mean', 
       tensor([0.0466, 0.0486, 0.0533, 0.0446, 0.0463, 0.0538, 0.0465, 0.0494, 0.0547, 0.0573, 0.0436, 0.0545, 0.0428, 0.0505, 0.0529, 0.0429])),
    ('running_var', tensor([0.9072, 0.9092, 0.9097, 0.9091, 0.9085, 0.9078, 0.9099, 0.9088, 0.9084,
        0.9078, 0.9073, 0.9068, 0.9078, 0.9060, 0.9078, 0.9066])), 
    ('num_batches_tracked', tensor(1))]), '_non_persistent_buffers_set': set(), '_backward_hooks': OrderedDict(), '_is_full_backward_hook': None, '_forward_hooks': OrderedDict(), '_forward_pre_hooks': OrderedDict(), '_state_dict_hooks': OrderedDict(), '_load_state_dict_pre_hooks': OrderedDict(), '_modules': OrderedDict(), 'num_features': 16, 'eps': 1e-05, 'momentum': 0.1, 'affine': True, 'track_running_stats': True}'''