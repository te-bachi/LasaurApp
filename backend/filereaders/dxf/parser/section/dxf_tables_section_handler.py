
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

import dxf_section_handler


class DXFTablesSectionHandler(dxf_section_handler.DXFSectionHandler):

    def __init__(self):
        from filereaders.dxf.dxf_constants import DXFConstants

        super(DXFTablesSectionHandler, self).__init__(DXFConstants.SECTION_TYPE_TABLES)

    def parseGroup(self, groupCode, value):
        pass
