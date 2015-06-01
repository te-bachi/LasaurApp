
__author__ = 'David S. Touretzky, Stefan Hechenberger <stefan@nortd.com>, Kevin Loney <kevin.loney@brainsinjars.com>, Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'


import math
import StringIO
import logging
import filereaders.dxf.parser.dxf_parser


logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


parser = filereaders.dxf.parser.dxf_parser.DXFParser()

class DXFReader:
    """Parse very simple DXF files with lines, arcs, and lwpolyline.

    Usage:
    reader = DXFReader(0.08)
    boundarys = reader.parse(open('filename').read())
    """

    def __init__(self, tolerance):
        # tolerance settings, used in tessalation, path simplification, etc         
        self.tolerance = tolerance
        self.tolerance2 = tolerance**2

        # parsed path data, paths by color
        # {'#ff0000': [[path0, path1, ..], [path0, ..], ..]}
        # Each path is a list of vertices which is a list of two floats.        
        self.boundarys = {'#000000':[]}
        self.black_boundarys = self.boundarys['#000000']



    def parse(self, dxfstring):

        l = parser.parse(dxfstring, self.tolerance)

        d = {'#000000': l}
        return {'boundarys': d}






