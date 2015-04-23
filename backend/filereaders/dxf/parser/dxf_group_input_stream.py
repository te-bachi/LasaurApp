
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

import StringIO

from filereaders.dxf.dxf_value import DXFValue

class DXFGroupInputStream:

    def __init__(self, buf):
        self.stringio = StringIO.StringIO(buf)

    def __iter__(self):
        return self

    def next(self):

        groupCode = self.stringio.readline()
        if not groupCode:
            raise StopIteration
        groupCode = int(groupCode.strip())

        value = self.stringio.readline()
        if not value:
            raise ValueError('Premature end of file!')
        value = DXFValue(value.strip())

        return groupCode, value
