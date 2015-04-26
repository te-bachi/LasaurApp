
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

import StringIO

from filereaders.dxf.dxf_value import DXFValue

class DXFGroupBuffer:

    def __init__(self, buf):
        self.stringio = StringIO.StringIO(buf)

    def __iter__(self):
        return self

    def next(self):
        """

        :return: a group code and the according value
        :rtype: :func:`list`
        :raises StopIteration: if the iterator is at the end of the buffer
        :raises ValueError: if the buffer ends abruptly/unexpected
        """
        groupCode = self.stringio.readline()
        if not groupCode:
            raise StopIteration
        groupCode = int(groupCode.strip())

        value = self.stringio.readline()
        if not value:
            raise ValueError('Premature end of file!')
        value = DXFValue(value.strip())

        return groupCode, value
