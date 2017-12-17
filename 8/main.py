# -*- coding: utf-8 -*-
import Graph

def main():
    g = Graph.Graph(4)
    g.matrix()
    g.makeSetNode()
    print(g.outputRibs())

if __name__ == '__main__':
    main()