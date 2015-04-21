
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

from ..dxf_tuple import DXFTuple

class DXFParser:

    def __init__(self):
        pass

    def parse(self, dxfstring):
        linecount   = 0
        line        = ""
        dxfTuple       = DXFTuple(dxfstring)
        isKey       = True

        for key, value in dxfTuple:
            print(key + ": " + value)



