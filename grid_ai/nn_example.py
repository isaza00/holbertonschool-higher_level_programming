#!/usr/bin/env python3
""" Module to create a grid for algo to move piece """

import tkinter as tk
import random
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

class DQN(nn.Module):
    """ deep q network model """
    def __init__(self):
        super().__init__()
        self.hl1 = nn.Linear(in_features=2, out_features=4)
        self.hl2 = nn.Linear(in_features=4, out_features=4)
        self.out = nn.Linear(in_features=4, out_features=4)

    def forward(self, t):
        t = self.hl1(t)
        t = F.relu(t)
        t = self.hl2(t)
        t = F.relu(t)
        t = self.out(t)
        return t

t = torch.tensor([0.1, 0.1], [0.3, 0.5])
print(t)
policy_net = DQN()
target_net = DQN()
#copy parameters from policy_net to target_net
target_net.load_state_dict(policy_net.state_dict())
#put target_net to give results not learning
target_net.eval()
optimizer = optim.Adam(params=policy_net.parameters(), lr=0.01)

with torch.no_grad():
    actions = policy_net(t)
    max_action = policy_net(t).argmax().item()
print(actions)
print(max_action)