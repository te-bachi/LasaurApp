
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

import dxf_point


class DXFVertex(dxf_point.DXFPoint):

    def __init__(self):

        super(DXFVertex, self).__init__()

        self.x = 0
        self.y = 0
        self.z = 0
        self.startWidth = 0.0
        self.endWidth = 0.0

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setZ(self, z):
        self.z = z

    def setStartWidth(self, startWidth):
        self.startWidth = startWidth

    def setEndWidth(self, endWidth):
        self.endWidth = endWidth

    def setPolyFaceMeshVertex0(self, mesh0):
        pass

    def setPolyFaceMeshVertex1(self, mesh1):
        pass

    def setPolyFaceMeshVertex2(self, mesh2):
        pass

    def setPolyFaceMeshVertex3(self, mesh3):
        pass

