
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

import dxf_entity_handler


class DXFArcHandler(dxf_entity_handler.DXFEntityHandler):

    ENTITY_VALUE = "ARC"

    def __init__(self):
        pass

    def startEntity(self, value):
        pass

    def endEntity(self):
        pass
