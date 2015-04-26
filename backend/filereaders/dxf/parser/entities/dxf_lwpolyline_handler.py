
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

from filereaders.dxf.parser.entities import dxf_entity_handler


class DXFLwpolylineHandler(dxf_entity_handler.DXFEntityHandler):

    def __init__(self, name):
        super(DXFLwpolylineHandler, self).__init__(name)

    def startEntity(self):
        pass

    def endEntity(self):
        pass
