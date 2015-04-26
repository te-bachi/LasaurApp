
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

from dxf_header import DXFHeader
from dxf_constants import DXFConstants

class DXFDocument:

    def __init__(self):
        self.header = DXFHeader()
        self.blocks = {}
        self.layers = {}

    def getHeader(self):
        return self.header

    def getBlock(self, blockName):
        return self.blocks[blockName]

    def getLayer(self, layerName):
        """

        :param layerName:
        :type layerName: str
        :return:
        """
        return self.layers[layerName]

    def addLayer(self, layer):
        """

        :param layer:
        :type layer: filereaders.dxf.dxf_layer.DXFLayer
        """
        self.layers[layer.getName()] = layer

