
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

from filereaders.dxf.parser.entities import dxf_entity_handler


class DXFLineHandler(dxf_entity_handler.DXFEntityHandler):

    def __init__(self):
        from filereaders.dxf.dxf_constants import DXFConstants

        super(DXFLineHandler, self).__init__(DXFConstants.ENTITY_TYPE_LINE)

    def startEntity(self):
        pass

    def endEntity(self):
        pass
