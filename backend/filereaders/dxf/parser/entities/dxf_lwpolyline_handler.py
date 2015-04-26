
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

from filereaders.dxf.parser.entities import dxf_entity_handler


class DXFLwpolylineHandler(dxf_entity_handler.DXFEntityHandler):

    def __init__(self):
        from filereaders.dxf.dxf_constants import DXFConstants

        super(DXFLwpolylineHandler, self).__init__(DXFConstants.ENTITY_TYPE_LWPOLYLINE)

    def startEntity(self):
        pass

    def endEntity(self):
        pass
