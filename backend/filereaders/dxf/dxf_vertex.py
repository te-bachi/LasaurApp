__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

import dxf_point

class DXFVertex(dxf_point.DXFPoint):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setZ(self, z):
        self.z = z

    def setStartWidh(self, startWidth):
        self.startWidth = startWidth

    def endWidth(self, endWidth):
        self.endWidth = endWidth
