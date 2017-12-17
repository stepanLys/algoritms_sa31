# -*- coding: utf-8 -*-

import random

class Array():
    def __init__(self):
        self.list = [round(random.uniform(0, 100), 2) for i in range(random.randint(2,100))]
        # self.list = [input('enter array: ')]
        self.list1 = list()
        self.list2 = list()
        self.n = input('n: ')

    def draw(self):
        return self.list

    def inputN(self):
        return self.n

    def separate(self):
        self.list1 = self.list[:int(self.inputN())]
        self.list2 = self.list[int(self.inputN()):]

        return self.list1, self.list2