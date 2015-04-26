__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

import dxf_entity
import dxf_constants


class DXFPolyline(dxf_entity.DXFEntity):

    def __init__(self):
        super(DXFPolyline, self).__init__()
        self.vertices = []
        self.startWidth = 0
        self.endWidth = 0

    def getType(self):
        return dxf_constants.DXFConstants.ENTITY_TYPE_POLYLINE

    def addVertex(self, vertex):
        self.vertices.append(vertex)

    def setStartWidh(self, startWidth):
        self.startWidth = startWidth

    def endWidth(self, endWidth):
        self.endWidth = endWidth
