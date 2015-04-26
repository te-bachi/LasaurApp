
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

from filereaders.dxf.parser.entities import dxf_entity_handler


class DXFSplineHandler(dxf_entity_handler.DXFEntityHandler):

    def __init__(self):
        from filereaders.dxf.dxf_constants import DXFConstants

        super(DXFSplineHandler, self).__init__(DXFConstants.ENTITY_TYPE_SPLINE)

    def startEntity(self):
        pass

    def endEntity(self):
        pass
