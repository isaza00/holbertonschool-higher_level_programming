#!/usr/bin/python3
""" Module to create a grid for algo to move piece """

import tkinter as tk
import random



class Piece:
    """ class to define movements of piece on the grid """
    q = {}
    r = 0
    start = 0

    def __init__(self, rows=5, columns=5, position=(0,0), goal=(None, None)):
        """ initialize object in position (row, column) """
        self.position = position
        self.rows = rows
        self.columns = columns
        self.goal = goal
        self.iteration = 0
        self.grid_position()

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
        self.__position = value

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

    def grid_position(self):
        """ according to position locates piece in matrix grid """
        self.grid = [[0] * self.__columns for i in range(self.__rows)]
        for i in range(self.__rows):
            for j in range(self.__columns):
                if i == self.__position[0] and j == self.__position[1]:
                    self.grid[i][j] = 1
        self.stating()
        self.grid_goal_position()
        return self.grid

    def stating(self):
        big_list = []
        for rows in self.grid:
            for items in rows:
                big_list.append(items)
        self.state = int(''.join(map(str, big_list)), 2)
        return self.state

    def grid_to_pos(self, grid):
        for i in range(self.__rows):
            for j in range(self.__columns):
                if grid[i][j] == 1:
                    return (i, j)

    def grid_goal_position(self):
        """ according to position locates piece in matrix grid """
        self.grid_goal = [[0] * self.__columns for i in range(self.__rows)]
        for i in range(self.__rows):
            for j in range(self.__columns):
                if i == self.__goal[0] and j == self.__goal[1]:
                    self.grid_goal[i][j] = 1
        return self.grid_goal

    def action_right(self):
        """ update grid with one movement to right """
        for i in range(self.__rows):
            for j in range(self.__columns):
                Piece.r = -1
                if self.grid[i][j] == 1 and j == self.__columns - 1:
                    Piece.r = -1
                    print("crash")
                    return self.grid
                if self.grid[i][j] == 1:
                    self.grid[i][j] = 0
                    self.grid[i][j+1] = 1
                    self.move_right()
                    return self.grid
        

    def action_left(self):
        """ update grid with one movement to right """
        for i in range(self.__rows):
            for j in range(self.__columns):
                Piece.r = -1
                if self.grid[i][j] == 1 and j == 0:
                    Piece.r = -1
                    print("crash")
                    return self.grid
                if self.grid[i][j] == 1:
                    self.grid[i][j] = 0
                    self.grid[i][j-1] = 1
                    self.move_left()
                    return self.grid

    def action_down(self):
        """ update grid with one movement to right """
        for i in range(self.__rows):
            for j in range(self.__columns):
                Piece.r = -1
                if self.grid[i][j] == 1 and i == self.__rows - 1:
                    Piece.r = -1
                    print("crash")
                    return self.grid
                if self.grid[i][j] == 1:
                    self.grid[i][j] = 0
                    self.grid[i+1][j] = 1
                    self.move_down()
                    return self.grid

    def action_up(self):
        """ update grid with one movement to right """
        for i in range(self.__rows):
            for j in range(self.__columns):
                Piece.r = -1
                if self.grid[i][j] == 1 and i == 0:
                    Piece.r = -1
                    print("crash")
                    return self.grid
                if self.grid[i][j] == 1:
                    self.grid[i][j] = 0
                    self.grid[i-1][j] = 1
                    self.move_up()
                    return self.grid

    def draw_grid(self):
        """ draws grid """
        self.step = 50
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
        self.positioning()
        column0 = self.__goal[1]*self.size + self.size/2
        row0 = self.__goal[0]*self.size + self.size/2
        self.canvas.create_text(column0, row0, text="GOAL", fill="red")

    def positioning(self):
        column0 = self.size * self.position[0] + 10
        column1 = column0 + self.size -20
        row0 = self.size * self.position[1] + 10
        row1 = row0 + self.size - 20
        self.dot = self.canvas.create_oval(row0, column0, row1, column1, fill='red')

    def restart(self):
        self.grid_position()
        self.positioning()

    def move_right(self):
        self.canvas.after(self.step, self.canvas.move, self.dot, self.size, 0)
    
    def move_left(self):
        self.canvas.after(self.step, self.canvas.move, self.dot, -self.size, 0)
    
    def move_up(self):
        self.canvas.after(self.step, self.canvas.move, self.dot, 0, -self.size)
    
    def move_down(self):
        self.canvas.after(self.step, self.canvas.move, self.dot, 0, self.size)

    def arrow(self):
        action = self.maxim_action(self.state)
        pos = self.grid_to_pos(self.grid)
        column0 = pos[1]*self.size + self.size/2
        row0 = pos[0]*self.size + self.size/2
        if pos in self.dic:
            self.canvas.delete(self.dic[pos])
        if action == "a_up":
            text = "^"
        elif action == "a_down":
            text = "v"
        elif action == "a_right":
            text = ">"
        elif action == "a_left":
            text = "<"
        self.dic[pos] = self.canvas.create_text(column0, row0, text=text, fill="blue")
        
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
        alpha, gamma = 0.8, 0.8
        self.actions = {
                    "a_right":self.periodic_right, 
                    "a_down":self.periodic_down,
                    "a_left":self.periodic_left,
                    "a_up":self.periodic_up
                    }
        if Piece.start == 0:
            Piece.start = 1
            self.action = random.choice(list(self.actions.keys()))
            Piece.q[(self.state, self.action)] = 0
        if (self.state, self.action) not in Piece.q:
            Piece.q[(self.state, self.action)] = 0
        q_s_a = Piece.q[(self.state, self.action)]
        self.arrow()
        state = self.state
        print("iteration:", self.iteration)
        print("actual state:", state)
        print("actual action:", self.action)
        self.actions[self.action]()
        if self.grid == self.grid_goal:
            print("Goal reached")
            Piece.r = 1
            self.restart()
        self.stating()
        next_state = self.state
        next_action = self.egreedy(next_state)
        if (next_state, next_action) not in Piece.q:
            Piece.q[(next_state, next_action)] = 0
        delta = alpha*(Piece.r + gamma*Piece.q[(next_state, next_action)] - q_s_a)
        Piece.q[(state, self.action)] = q_s_a + delta
        print("reward:", Piece.r)
        print("Q actual state-action", Piece.q[(state, self.action)])
        print("next state:", next_state)
        print("next action:", next_action)
        print("Q next state-action", Piece.q[(next_state, next_action)])
        print()
        self.state = next_state
        self.action = next_action

    def egreedy(self, next_state):
        if self.iteration < 100000:
            epsilon = 0.9
        else:
            self.step = 800
            epsilon = 0.1
        self.iteration += 1
        aleatory = random.uniform(0, 1)
        choice = random.choice(list(self.actions.keys()))
        if  aleatory < epsilon:
            return choice
        else:
            max_action = self.maxim_action(next_state)
            return max_action
    
    def maxim_action(self, state):
        sub_dic = {}
        max_action = "a_right"
        for key in Piece.q:
                if key[0] == state:
                    sub_dic[key[1]] = Piece.q[key]
        if sub_dic:
            max_action = max(sub_dic, key=sub_dic.get)
        return max_action

    def open_window(self):
        self.window.mainloop()

piece = Piece(rows=30, columns=30)
piece.draw_grid()
piece.periodic_square()
piece.open_window()


