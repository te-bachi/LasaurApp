
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

from dxf_header import DXFHeader


class DXFDocument:
    layers = 0
    viewports = 0
    bounds = 0
    margin = 0

    def __init__(self):
        self.header = DXFHeader()
        self.tables = ()
        self.blocks = ()
        self.entities = ()

    def getHeader(self):
        return self.header

    def getTables(self):
        return self.tables

    def getBlocks(self):
        return self.blocks

    def getEntities(self):
        return self.entities
