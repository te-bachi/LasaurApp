
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

import filereaders.dxf.parser.dxf_handler

class DXFSectionHandler(filereaders.dxf.parser.dxf_handler.DXFHandler):

    GROUP_CODE_ENTITY_START     = 0
    GROUP_CODE_NAME     = 2
    SECTION_START       = "SECTION"
    SECTION_END         = "ENDSEC"

    def __init__(self):
        from dxf_header_section_handler import DXFHeaderSectionHandler
        from dxf_table_section_handler import DXFTableSectionHandler
        from dxf_objects_section_handler import DXFObjectsSectionHandler
        from dxf_entities_section_handler import DXFEntitiesSectionHandler

        self.section = None
        self.sectionStarts = False
        self.map = {
            DXFHeaderSectionHandler.SECTION_VALUE:      DXFHeaderSectionHandler(),
            DXFTableSectionHandler.SECTION_VALUE:       DXFTableSectionHandler(),
            DXFObjectsSectionHandler.SECTION_VALUE:     DXFObjectsSectionHandler(),
            DXFEntitiesSectionHandler.SECTION_VALUE:    DXFEntitiesSectionHandler()
        }

    def startSection(self):
        pass

    def endSection(self):
        pass

    def parseGroup(self, groupCode, value):
        if groupCode == self.GROUP_CODE_ENTITY_START and value == self.SECTION_START:
            self.sectionStarts = True

        elif groupCode == self.GROUP_CODE_ENTITY_START and value == self.SECTION_END:
            self.section = None

        elif groupCode == self.GROUP_CODE_NAME and self.sectionStarts:
            self.sectionStarts = False
            try:
                self.section = self.map[value]
            except KeyError:
                pass

        elif self.section:
            self.section.parseGroup(groupCode, value)


