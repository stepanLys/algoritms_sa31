# -*- coding: utf-8 -*-

import xml.etree.ElementTree as et

class Average():
    def __init__(self, file):
        self.tree = et.parse(file)
        self.num = list()

    def parseXML(self):
        root = self.tree.getroot()

        return root

    def serchAver(self):
        for i in self.parseXML().findall('node'):
            val = float(i.find('value').text)
            self.num.append(val)

        print(self.num)

        return (sum(self.num)/len(self.num))