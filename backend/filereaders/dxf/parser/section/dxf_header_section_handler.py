
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

import dxf_section_handler


class DXFHeaderSectionHandler(dxf_section_handler.DXFSectionHandler):

    def __init__(self, name):
        super(DXFHeaderSectionHandler, self).__init__(name)

    def startSection(self):
        pass

    def endSection(self):
        pass

    def parseGroup(self, groupCode, value):
        pass
