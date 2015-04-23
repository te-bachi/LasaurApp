
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

import dxf_section_handler


class DXFEntitiesSectionHandler(dxf_section_handler.DXFSectionHandler):

    SECTION_VALUE = "ENTITIES"

    def __init__(self):
        from entities.dxf_entity_handler import DXFEntityHandler

        self.entity = DXFEntityHandler()

    def startEntitySection(self):
        pass

    def endEntitySection(self):
        pass

    def parseGroup(self, groupCode, value):
        self.entity.parseGroup(groupCode, value)


