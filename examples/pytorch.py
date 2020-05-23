from chocolate import filter_args
import torch
import torch.optim as optim
from torch.optim.lr_scheduler import ReduceLROnPlateau


args = {"lr": 0.1, "min_lr": 0.001}
var = torch.FloatTensor([0])
optimizer = optim.SGD([var], **filter_args(args, optim.SGD))
lr_scheduler = ReduceLROnPlateau(optimizer, **filter_args(args, ReduceLROnPlateau))
