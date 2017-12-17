# -*- coding: utf-8 -*-
import Tree, Array


def main():
    t = Tree.Average('tree.xml')
    print(t.serchAver())


    a = Array.Array()
    print(a.draw())
    print(a.separate())


if __name__ == '__main__':
    main()