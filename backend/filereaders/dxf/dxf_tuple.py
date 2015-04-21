
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

import StringIO

class DXFTuple:

    def __init__(self, buf):
        self.stringio = StringIO.StringIO(buf)

    def __iter__(self):
        return self

    def next(self):

        key = self.stringio.readline()
        if not key:
            raise StopIteration
        key = key.strip()

        value = self.stringio.readline()
        if not value:
            raise ValueError('Premature end of file!')
        value = value.strip()

        return key, value
