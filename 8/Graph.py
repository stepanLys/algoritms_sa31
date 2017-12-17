# -*- coding: utf-8 -*-

import numpy as np
import random

class Graph():
    def __init__(self, amount):
        # self.adjacencyMatrix = [[random.randrange(0, 2) for y in range(amount)] for x in range(amount)]
        self.adjacencyMatrix = np.random.randint(2, size=(amount, amount))
        self.amount = amount
        self.ribs = list()

    def matrix(self):
        '''
        This function randomly fills in the 0 or 1 adjacency matrix
        :return: adjacency matrix
        '''
        for i in range(self.amount):
            print(self.adjacencyMatrix[i])

    def makeSetNode(self):
        for i in range(self.amount):
            for j in range(self.amount):
                if self.adjacencyMatrix[i][j] == 0:
                    continue
                else:
                    self.ribs.append((i,j))

    def outputRibs(self):
        return self.ribs