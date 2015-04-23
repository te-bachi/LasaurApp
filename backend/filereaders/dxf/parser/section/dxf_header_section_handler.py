
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

import dxf_section_handler


class DXFHeaderSectionHandler(dxf_section_handler.DXFSectionHandler):

    SECTION_VALUE = "HEADER"

    def __init__(self):
        pass

    def parseGroup(self, groupCode, value):
        pass
