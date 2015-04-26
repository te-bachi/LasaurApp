__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

from filereaders.dxf.parser.table import dxf_table_handler


class DXFLayerHandler(dxf_table_handler.DXFTableHandler):

    def __init__(self):
        pass

    def parseGroup(self, groupCode, value):
        pass
