# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.messagebox as tkm
import numpy as np
import random

# 0: vazio
# 1: snake
# 2: pill
# -1: fora do quadro
class Board:
    def __init__(self, N):
        self.N = N
        self.board = np.zeros([N, N])
        
    def set(self, i, j, valor):
        if i >= 0 and i < self.N and j >= 0 and j < self.N:
            self.board[i][j] = valor
            
    def get(self, i, j):
        if i >= 0 and i < self.N and j >= 0 and j < self.N:
            return self.board[i][j]
        else:
            return -1

# Direcao:
# 0: norte
# 1: leste
# 2: sul
# 3: oeste

class Snake:
    def __init__(self, i, j, direction):
        self.direction = direction
        self.body = [(i,j)]

    def next_head(self):
        i, j = self.body[-1]
        if self.direction == 0:
            i -= 1
        elif self.direction == 1:
            j += 1
        elif self.direction == 2:
            i += 1
        else:
            j -= 1
        return i, j

    def get_tail(self):
        return self.body[0]

    def add_head(self):
        i, j = self.next_head()
        self.body.append((i,j))
        
    def remove_tail(self):
        del self.body[0]
        
    def add_to_board(self, board):
        for square in self.body:
            i = square[0]
            j = square[1]
            board.set(i, j, 1)
            
    def contains(self, i, j):
        for square in self.body:
            if i == square[0] and j == square[1]:
                return True
        return False
    
    def set_direction(self, direction):
        self.direction = direction
        
    def get_size(self):
        return len(self.body)
    
class SnakeGame:
    def __init__(self):
        self.width = 400
        self.height = 400
        self.N = 10
        self.T = 300
        self.max_size = 10
        
        self.board = Board(self.N)
        self.snake = Snake(self.N//2, self.N//2, 0)
        
        self.snake.add_to_board(self.board)
        
        self.add_pill()
        
        self.window = tk.Tk()
        self.window.title("Snake Insper")
        self.window.geometry("400x400+100+100")
        self.window.rowconfigure(0, minsize=self.height)
        self.window.columnconfigure(0, minsize=self.width)
        self.window.grid()
        
        self.window.bind("<Up>", self.key_up)
        self.window.bind("<Right>", self.key_right)
        self.window.bind("<Down>", self.key_down)
        self.window.bind("<Left>", self.key_left)
        
        self.canvas = tk.Canvas(self.window)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        
        self.draw_board()
        
    def key_up(self, event):
        self.snake.set_direction(0)
    
    def key_right(self, event):
        self.snake.set_direction(1)
    
    def key_down(self, event):
        self.snake.set_direction(2)
    
    def key_left(self, event):
        self.snake.set_direction(3)
    
    def draw_square(self, i, j, value):
        x0 = j * self.width // self.N
        y0 = i * self.height // self.N
        x1 = x0 + self.width // self.N
        y1 = y0 + self.height // self.N
        
        if value == 0:
            color = "white"
        elif value == 1:
            color = "blue"
        elif value == 2:
            color = "red"
        
        self.canvas.create_rectangle(x0, y0, x1, y1, 
                                     fill=color, outline=color)
    
    def draw_board(self):
        self.canvas.create_rectangle(0, 0, 
                                     self.width-1, self.height-1, 
                                     fill="white",
                                     outline="white")
        for i in range(self.N):
            for j in range(self.N):
                value = self.board.get(i, j)
                self.draw_square(i, j, value)

    def add_pill(self):
        while True:
            i = random.randint(0, self.N - 1)
            j = random.randint(0, self.N - 1)
            if not self.snake.contains(i, j):
                self.board.set(i, j, 2)
                break
            
    def animation(self):
        i, j = self.snake.next_head()
        value = self.board.get(i, j)
        if value == 1 or value == -1:
            tkm.showinfo(title="Game over!", message="You lose!")
            self.window.quit()
        else:
            self.snake.add_head()
            self.board.set(i, j, 1)
            if value != 2:
                i_tail, j_tail = self.snake.get_tail()
                self.snake.remove_tail()
                self.board.set(i_tail, j_tail, 0)
            else:
                self.add_pill()

            if self.snake.get_size() == self.max_size:
                tkm.showinfo(title="Game over!", message="You win!")
                self.window.quit()
            self.draw_board()
            self.window.after(self.T, self.animation)
    
    def iniciar(self):
        self.window.after(self.T, self.animation)
        self.window.mainloop()
        
app = SnakeGame()
app.iniciar()