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
        self.hl1 = nn.Linear(in_features=25, out_features=25)
        #self.hl2 = nn.Linear(in_features=25, out_features=25)
        self.out = nn.Linear(in_features=25, out_features=4)

    def forward(self, t):
        t = self.hl1(t)
        t = F.relu(t)
        #t = self.hl2(t)
        #t = F.relu(t)
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
    max_length = 1000
    #Define alpha and gamma
    alpha, gamma = 0.9, 0.9
    #Defines batch size
    batch_size = 2
    #update target_net params when:
    update_target_net = 200
    #speed for state change
    speed = 10

    def __init__(self, rows=5, columns=5, position=(0,0), goal=(None, None)):
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
        row_piece = position[0] / self.__rows
        column_piece = position[1] / self.__columns
        x = [row_piece, column_piece]
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
        self.duration += 1
        #initializes an episode with random action
        if Piece.start ==0:
            Piece.start = 1
            self.action_number = random.randrange(4)
            self.action = actions[self.action_number]
        #save current state
        state = self.state
        #take action
        action = actions[self.action_number]
        self.actions[action]()
        
        self.stating(self.__position)
        next_state = self.state
        next_action_number = self.egreedy(next_state)
        #check if reach terminal step
        if Piece.r == 1:
            self.restart()
            print("DURATION:", self.duration)
            self.duration = 0
        # checks if memory reached limit and pop oldest item
        if len(Piece.replay_memory) > Piece.max_length:
            Piece.replay_memory.pop(0)
        # save tuple et if not terminal state
        
        Piece.replay_memory.append((state,
                                    torch.tensor([self.action_number]),
                                    torch.tensor([Piece.r]),
                                    next_state))
        print("STATE:", Piece.replay_memory[-1][0])
        print("ACTION:", actions[Piece.replay_memory[-1][1].item()])
        print("NEXT STATE:", Piece.replay_memory[-1][3])
        print("REWARD", Piece.replay_memory[-1][2].item())
        if len(Piece.replay_memory) > Piece.batch_size:
            self.training()
        if self.iteration % Piece.update_target_net == 0:
            target_net.load_state_dict(policy_net.state_dict())
        self.state = next_state
        self.action_number = next_action_number
        self.reward = Piece.r

    def training(self):
        """ take a batch of replay memory and use NN """
        experiences = random.sample(Piece.replay_memory, Piece.batch_size)
        batch = self.extract(experiences)
        states = torch.stack(list(batch[0]))
        next_states = torch.stack(list(batch[3]))
        current_q = policy_net(states)
        next_q = target_net(next_states)
        print("CURRENT_Q:", current_q)
        print("NEXT_Q:", next_q)
        
        rewards = torch.stack(list(batch[2]))
        print("REWARD", rewards)
        target_q = next_q * Piece.gamma + rewards
        print("Target_Q:", target_q)
        loss = F.mse_loss(target_q, current_q)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        #if self.iteration % 10 == 0:
        print("LOSSSSSS:", loss)

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

piece = Piece(rows=5, columns=5, position=(0, 0))
piece.draw_grid()
piece.periodic_square()
piece.open_window()


