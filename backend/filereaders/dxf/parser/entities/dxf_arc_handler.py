
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

from filereaders.dxf.parser.entities import dxf_entity_handler


class DXFArcHandler(dxf_entity_handler.DXFEntityHandler):

    def __init__(self, name):
        super(DXFArcHandler, self).__init__(name)

    def startEntity(self, value):
        pass

    def endEntity(self):
        pass
