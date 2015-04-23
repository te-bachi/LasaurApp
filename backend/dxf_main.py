
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

import sys
print(sys.path)

import filereaders.dxf.parser.dxf_parser

f = open("/home/andreas/Downloads/booklets_A7_both_V2.dxf")

dxfstring = f.read()

parser = filereaders.dxf.parser.dxf_parser.DXFParser()
parser.parse(dxfstring)

f.close()
