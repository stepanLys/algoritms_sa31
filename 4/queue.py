import heapq, random
import numpy as np

class Queue():
    '''
        Class to work with a priority queue
    '''
    def __init__(self):
        self.tree = list()
        self.basic_index = 1
        self.priority = int()
        self.val = int()

    def set(self, len):
        while self.basic_index < len:
            self.priority = random.randint(1, 100)
            self.val = random.randint(1, 100)
            heapq.heappush(self.tree, (self.priority, self.basic_index, self.val))   # priority,  basic_index, value
            self.basic_index += 1

    def outputQueue(self):
        ''' Just out binary tree in array format  '''
        return self.tree

    def sortMax(self):
        ''' Sort by maximum priority '''
        return heapq.nlargest(len(self.tree), self.tree)[1]

    def sortMin(self):
        ''' Sort by minimum priority '''
        return heapq.nsmallest(len(self.tree), self.tree)

    def deleteFromQueue(self):
        ''' Queue removal using the fifo method '''
        indexArr = list()
        for i in range(len(self.tree)):
            heapq.heappush(indexArr, self.tree[i][1])
        indexArr = sorted(indexArr)
        print(indexArr[0])
        for i in range(len(self.tree)):
            if self.tree[i][1] == indexArr[0]:
                indexArr.pop()
                return self.tree.pop(i)