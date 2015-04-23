
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

import dxf_entity_handler


class DXFLwpolylineHandler(dxf_entity_handler.DXFEntityHandler):

    ENTITY_VALUE = "LWPOLYLINE"

    def __init__(self):
        pass

    def startEntity(self):
        pass

    def endEntity(self):
        pass
