import os
import time
from colorama  import *
import math

class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

        self.position = [0, 1]

        # self._canvas[int((self._x + 1) /2)][int((self._y +1) /2)] = 'x' marks centre of the canvas

    def hitsWall(self, point):
        return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y

    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = Fore.WHITE + '.'
        self.mark = Fore.RED + '*'
        self.framerate = 0.1
        self.pos = [16 , 16]

    def up(self):
        pos = [self.pos[0], self.pos[1]-1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def down(self):
        pos = [self.pos[0], self.pos[1]+1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def right(self):
        pos = [self.pos[0]+1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def left(self):
        pos = [self.pos[0]-1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos, self.mark)
        self.canvas.print()
        time.sleep(self.framerate)

    def drawSquare(self, size): #produces a simple square

        self.pos = [16 - int((size/2)) , 16 - int((size/2))]
        for i in range(1 ,size):
            self.right()
        for i in range(1, size):
            self.down()
        for i in range(1, size):
            self.left()
        for i in range(1, size):
            self.up()

canvas = Canvas(31, 31) #change size of board
scribe = TerminalScribe(canvas)

scribe.drawSquare(3)


