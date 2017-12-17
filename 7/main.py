# -*- coding: utf-8 -*-
from Tree import *

def main():
    tr = Tree()
    n1 = tr.root
    n2 = TreeNode("B")
    n3 = TreeNode("C")
    n4 = TreeNode("D")
    n5 = TreeNode("E")
    n6 = TreeNode("F")
    n7 = TreeNode("G")

    n1.add_child(n2)
    n1.add_child(n3)
    n2.add_child(n4)
    n2.add_child(n5)
    n3.add_child(n6)
    n3.add_child(n7)

    print(tr)

if __name__ == '__main__':
    main()