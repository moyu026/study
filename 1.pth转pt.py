import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
from torchsummary import summary

model1 = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True)
model1 = model1.eval().cuda()

PATH_MODEL2 = 'E:\pythonwork\helmet_classifier\model\\resnet18_helmet_3.pth'

class_names = ['other', 'helmet']
num_classes = len(class_names)
net_shell = torchvision.models.resnet18(False).eval()
layerFC = net_shell.fc.in_features  # 修改最后一层的分类输出层
net_shell.fc = torch.nn.Linear(layerFC, num_classes)  # 512 --> 2
net_shell.load_state_dict(torch.load(PATH_MODEL2))
model2 = net_shell.cuda()

model2.load_state_dict(torch.load(PATH_MODEL2))

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# traced_script_module = torch.jit.trace(model2, torch.ones(1, 3, 28, 28).to(device))  # [1,3,224,224]
traced_script_module = torch.jit.script(model2)
traced_script_module.save("mnist_cnn.pt")

