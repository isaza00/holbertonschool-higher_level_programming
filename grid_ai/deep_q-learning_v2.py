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
        self.hl1 = nn.Linear(in_features=400, out_features=400)
        self.hl2 = nn.Linear(in_features=400, out_features=400)
        self.out = nn.Linear(in_features=400, out_features=4)

    def forward(self, t):
        t = self.hl1(t)
        t = F.relu(t)
        t = self.hl2(t)
        t = F.relu(t)
        t = self.out(t)
        return t

policy_net = DQN()
target_net = DQN()
#copy parameters from policy_net to target_net
target_net.load_state_dict(policy_net.state_dict())
#put target_net to give results not learning
target_net.eval()
optimizer = optim.Adam(params=policy_net.parameters(), lr=0.01)

class Piece:
    """ class to define movements of piece on the grid """
    q = {}
    r = 0
    start = 0
    #initializze replay memory
    replay_memory = []
    max_length = 10000
    #Define alpha and gamma
    alpha, gamma = 0.9, 0.9
    #Defines batch size
    batch_size = 100
    #update target_net params when:
    update_target_net = 10
    #speed for state change
    speed = 20

    def __init__(self, rows=20, columns=20, position=(0,0), goal=(None, None)):
        """ initialize object in position (row, column) """
        self.state = 0
        self.position = position
        self.rows = rows
        self.columns = columns
        self.goal = goal
        self.iteration = 0
        self.stating(self.__position)
        self.duration = 0
        self.reward = 0

    @property
    def position(self):
        """ return coordenate of position """
        return self.__position

    @property
    def rows(self):
        """ return number of rows of grid """
        return self.__rows

    @property
    def columns(self):
        """ return number of rows of grid """
        return self.__columns

    @property
    def goal(self):
        """ return coordenate of goal """
        return self.__goal

    @position.setter
    def position(self, value):
        """ set position coordenates with (row, column) """
        self.__position = list(value)

    @rows.setter
    def rows(self, value):
        """ set number of rows """
        self.__rows = value

    @columns.setter
    def columns(self, value):
        """ set number of columns """
        self.__columns = value
    
    @goal.setter
    def goal(self, value):
        """ set position of goal with (row, column) """
        if value == (None, None):
            self.__goal = (self.__rows - 1, self.__columns - 1)
        else:
            self.__goal = value

    def stating(self, position):
        """ return a tensor with X entries """
        self.state = self.matrix_gen(position)

    def matrix_gen(self, position):
        """ according to position locates piece in matrix grid """
        self.grid = [[0] * self.__columns for i in range(self.__rows)]
        for i in range(self.__rows):
            for j in range(self.__columns):
                if i == self.__position[0] and j == self.__position[1]:
                    self.grid[i][j] = 1
        matrix = torch.tensor(self.grid, dtype=torch.float)
        matrix = matrix.flatten()
        return matrix

    def action_right(self):
        """ update X tensor with one movement to right """
        Piece.r = -1
        if self.__position[1] < self.__columns - 1:
            self.__position[1] += 1
            self.move_right()
            if self.__position == list(self.__goal):
                Piece.r = 1
        else:
            print("crash")


    def action_left(self):
        """ update X tensor with one movement to right """
        Piece.r = -1
        if self.__position[1] > 0:
            self.__position[1] -= 1
            self.move_left()
            if self.__position == list(self.__goal):
                Piece.r = 1
        else:
            print("crash")


    def action_down(self):
        """ update X tensor with one movement to right """
        Piece.r = -1
        if self.__position[0] < self.__rows - 1:
            self.__position[0] += 1
            self.move_down()
            if self.__position == list(self.__goal):
                Piece.r = 1
        else:
            print("crash")

    def action_up(self):
        """ update X tensor with one movement to right """
        Piece.r = -1
        if self.__position[0] > 0:
            self.__position[0] -= 1
            self.move_up()
            if self.__position == list(self.__goal):
                Piece.r = 1
        else:
            print("crash")


    def draw_grid(self):
        """ draws grid """
        self.step = Piece.speed
        self.dic = {}
        self.window = tk.Tk()
        self.window.title("grid for Sarsa algo")
        frame = tk.LabelFrame(self.window, text="Frame", padx=20, pady=20)
        frame.pack()
        self.grid_width = 500
        self.grid_height = 500
        self.width = self.grid_width / self.__rows
        self.height = self.grid_height / self.__columns
        self.canvas = tk.Canvas(frame, height=self.grid_height+10, width=self.grid_width+10, borderwidth=0, highlightthickness=0)
        self.canvas.grid(row=0, column=0, padx=0, pady=0)
        self.size = min(self.width, self.height)
        grid = [0, 0, self.size, self.size]
        canvas_list = []
        x = 0
        for i in range(self.__rows):
            canvas_list.append([])
            for j in range(self.__columns):
                canvas_list[x].append(self.canvas.create_rectangle(grid))
                grid[0] += self.size
                grid[2] += self.size
            x += 1
            grid[0] = 0
            grid[2] = self.size
            grid[1] += self.size
            grid[3] += self.size
        self.positioning((0,0))
        column0 = self.__goal[1]*self.size + self.size/2
        row0 = self.__goal[0]*self.size + self.size/2
        self.canvas.create_text(column0, row0, text="GOAL", fill="red")

    def positioning(self, position):
        column0 = self.size * position[0] + 10
        column1 = column0 + self.size -20
        row0 = self.size * position[1] + 10
        row1 = row0 + self.size - 20
        self.dot = self.canvas.create_oval(row0, column0, row1, column1, fill='red')

    def restart(self):
        self.__position = [0, 0]
        self.stating(self.__position)
        self.positioning(self.__position)

    def move_right(self):
        self.canvas.after(0, self.canvas.move, self.dot, self.size, 0)
    
    def move_left(self):
        self.canvas.after(0, self.canvas.move, self.dot, -self.size, 0)
    
    def move_up(self):
        self.canvas.after(0, self.canvas.move, self.dot, 0, -self.size)
    
    def move_down(self):
        self.canvas.after(0, self.canvas.move, self.dot, 0, self.size)

    def arrow(self, max_action):
        actions = ["a_right", "a_down", "a_left", "a_up"]
        action = actions[max_action]
        pos = self.__position
        column0 = pos[1]*self.size + self.size/2
        row0 = pos[0]*self.size + self.size/2
        if tuple(pos) in self.dic:
            self.canvas.delete(self.dic[tuple(pos)])
        if action == "a_up":
            text = "^"
        elif action == "a_down":
            text = "v"
        elif action == "a_right":
            text = ">"
        elif action == "a_left":
            text = "<"
        self.dic[tuple(pos)] = self.canvas.create_text(column0, row0, text=text, fill="blue")
        
    def periodic_up(self):
        self.action_up()
        self.window.after(self.step, self.periodic_square)

    def periodic_down(self):
        self.action_down()
        self.window.after(self.step, self.periodic_square)

    def periodic_right(self):
        self.action_right()
        self.window.after(self.step, self.periodic_square)

    def periodic_left(self):
        self.action_left()
        self.window.after(self.step, self.periodic_square)

    def periodic_square(self):
        actions = ["a_right", "a_down", "a_left", "a_up"]
        self.actions = {
                    "a_right":self.periodic_right, 
                    "a_down":self.periodic_down,
                    "a_left":self.periodic_left,
                    "a_up":self.periodic_up
                    }
        #update current state
        self.stating(self.__position)
        #save current state
        current_state = self.state
        #print("Current State: ", self.state)
        # select action by egreedy method
        action_number = self.egreedy(current_state)
        current_action = actions[action_number]
        print("Take action: ", current_action)
        # execute action and update state
        self.actions[current_action]()
        self.stating(self.__position)
        #Observe reward and next state
        reward = Piece.r
        next_state = self.state
        #print("Next State: ", next_state)
        #print("Reward: ", reward)
        #Store event in the replay memory and delete oldest if len > max_length
        Piece.replay_memory.append((current_state,
                                   torch.tensor([action_number], dtype=torch.int64),
                                   torch.tensor([reward], dtype=torch.float),
                                   next_state))
        if len(Piece.replay_memory) >= Piece.max_length:
            Piece.replay_memory.pop(0)
        #Sample a random batch of events from replay memory
        if len(Piece.replay_memory) > Piece.batch_size:
            self.training()
        #copy weights from policy network to target network
        if self.iteration % Piece.update_target_net == 0:
            target_net.load_state_dict(policy_net.state_dict())
        #If final state was reached start again
        if reward == 1:
            print("TARGE REACHED")
            self.restart()
        print()
        print()

    def training(self):
        """ take a batch of replay memory and use NN """
        lista = []
        super_lista = []
        #take aleatory samples from replay memory of size batch_size
        experiences = random.sample(Piece.replay_memory, Piece.batch_size)
        #calls an organized tuple like (t_states, t_actions, t_rewards, t_next_states)
        batch = self.extract(experiences)
        #group all tensors in just one
        states = torch.stack(list(batch[0]))
        actions = torch.stack(list(batch[1]))
        
        next_states = torch.stack(list(batch[3]))
        rewards = torch.stack(list(batch[2]))
        #print("states: ", states)
        #print("actions: ", actions)
        #print("rewards: ", rewards)
        #get current Q for action A in tuple
        current_q = policy_net(states).gather(dim=1, index=actions)
        #print("CURRENT Q:", current_q)
        #get best action for next state
        next_q = target_net(next_states).max(dim=1)[0].unsqueeze(-1).detach()
        #print("NEXT Q:", next_q)
        #convert next_q and rewards tensors to lists for calculation
        next_q = next_q.tolist()
        rewards = rewards.tolist()
        #calculate target_q for each value in next_q
        for i, row in enumerate(next_q):
            for item in row:
                if rewards[i][0] != 1:
                    target_q = item * Piece.gamma + rewards[i][0]
                else:
                    target_q = 1
                lista.append(target_q)
            super_lista.append(lista)
            lista = []
        #retransforms target_q into a tensor
        target_q = torch.tensor(super_lista, dtype=torch.float)
        #print("TARGET Q:", target_q)
        #calculate loss with MSE
        loss = F.mse_loss(current_q, target_q)
        #put gradient to zero for each pass
        optimizer.zero_grad()
        #make gradient with loss
        loss.backward()
        #optimize weights
        optimizer.step()
        print("LOSS:", loss.item())

    def extract(self, experiences):
        """ extract experiences to tuple of tensors """
        batch = tuple(zip(*experiences))
        t_states = batch[0]
        t_actions = batch[1]
        t_rewards = batch[2]
        t_next_states = batch[3]
        return (t_states, t_actions, t_rewards, t_next_states)


    def egreedy(self, state):
        """ chooses the action by epsilon greedy method """
        print("Iteration:", self.iteration)
        if self.iteration < 10000:
            epsilon = 0.8
        else:
            self.step = 500
            epsilon = 0.1
        self.iteration += 1
        aleatory = random.uniform(0, 1)
        if  aleatory < epsilon:
            random_action = random.randrange(4)
            return random_action
        else:
            with torch.no_grad():
                max_action = policy_net(state).argmax().item()
                self.arrow(max_action)
                return max_action


    def open_window(self):
        self.window.mainloop()

piece = Piece(position=(0, 0))
piece.draw_grid()
piece.periodic_square()
piece.open_window()


