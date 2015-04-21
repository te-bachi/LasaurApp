
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

from dxf.parser.dxf_parser import DXFParser

f = open("/home/andreas/Downloads/booklets_A7_both_V2.dxf")

dxfstring = f.read()

parser = DXFParser()
parser.parse(dxfstring)

f.close()
