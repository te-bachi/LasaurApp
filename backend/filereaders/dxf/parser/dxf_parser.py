
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

#
#    0 -    9   String
#   10 -   39   Double precision 3D point value
#   40 -   59   Double-precision floating-point value
#   60 -   79   16-bit integer value
#   90 -   99   32-bit integer value
#  100          String
# 102           String
# 105           String
# 110-119       Double precision floating-point value
#
class DXFParser:

    def __init__(self):
        from section.dxf_section_handler import DXFSectionHandler

        self.dxfSectionHandler = DXFSectionHandler()
        pass

    def parse(self, dxfstring):
        from dxf_group_input_stream import DXFGroupInputStream

        linecount   = 0
        dxfTuple    = DXFGroupInputStream(dxfstring)

        for groupCode, value in dxfTuple:
            linecount += 1
            #print(groupCode + ": " + value)
            self.dxfSectionHandler.parseGroup(groupCode, value)




