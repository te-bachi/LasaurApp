
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

import sys
print(sys.path)

import filereaders.dxf.parser.dxf_parser
argc = len(sys.argv)
print("Number of arguments: " + str(argc))
for arg in sys.argv:
    print(arg)

f = open(sys.argv[1])

dxfstring = f.read()

parser = filereaders.dxf.parser.dxf_parser.DXFParser()
parser.parse(dxfstring)

f.close()
