from Window import Window
from Board import Board
from agent import agent
from QLearner import QLearner
import pygame
import time
import sys

pygame.init()
w = Window()
a = agent()
b = Board()
b.createPenaltyCells()
w.drawSurface(b, a)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    q = QLearner(b)
    qTable = q.learn()
    dirToGo = {}
    for k, v in qTable.items():
        dirToGo[k] = max(v, key=v.get)
        print("k: {}, v: {}".format(k, v))
    #
    # print("____________________________________-")
    # for k, v in dirToGo.items():
    #     print("k: {}, v: {}".format(k,v))

    currNode = (a.getCurrCoords())

    while (not b.isTerminalCell(currNode)):
        a.move(dirToGo[currNode])
        currNode = a.getCurrCoords()
        # print(currNode)
        w.colorCell(currNode, (0, 0, 255))
        pygame.display.update()

    if (b.isTerminalCell(currNode)):
        time.sleep(20)
        sys.exit()
