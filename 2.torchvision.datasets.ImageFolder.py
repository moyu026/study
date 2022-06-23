from torchvision import datasets

datapath = r'E:\github\dataset\\test'
train_dataset = datasets.ImageFolder(datapath)
flower_list = train_dataset.class_to_idx

train_num = len(train_dataset)

