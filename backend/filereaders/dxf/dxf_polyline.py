__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

import dxf_entity


class DXFPolyline(dxf_entity.DXFEntity):

    def __init__(self):
        self.startWidth = 0
        self.endWidth = 0

    def setStartWidh(self, startWidth):
        self.startWidth = startWidth

    def endWidth(self, endWidth):
        self.endWidth = endWidth
