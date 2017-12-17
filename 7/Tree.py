# -*- coding: utf-8 -*-

class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

class Tree:
    def __init__(self):
        self.root = TreeNode('ROOT')

    def get_leaf_nodes(self):
        leafs = []
        self._collect_leaf_nodes(self.root, leafs)
        return leafs

    def _collect_leaf_nodes(self, node, leafs):
        if node is not None:
            if len(node.children) == 0:
                leafs.append(node)
            for n in node.children:
                self._collect_leaf_nodes(n, leafs)

    def printLeafs(self):
        print('My leaf: ', end='')
        for c in self.get_leaf_nodes():
            print(c.data, end=' ')

    def __str__(self):
        self.printLeafs()
        return str()