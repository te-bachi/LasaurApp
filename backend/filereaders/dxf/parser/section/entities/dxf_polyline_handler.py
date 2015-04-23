
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

import dxf_entity_handler

from filereaders.dxf.dxf_value import DXFValue
from filereaders.dxf.dxf_polyline import DXFPolyline
from filereaders.dxf.dxf_vertex import DXFVertex

class DXFPolylineHandler(dxf_entity_handler.DXFEntityHandler):

    ENTITY_VALUE                                = "POLYLINE"
    ENTITY_VERTEX                               = "VERTEX"
    END_SEQUENCE                                = "SEQEND"

    GROUP_CODE_END_SEQUENCE_CODE                = -2
    GROUP_CODE_VERTEX_BULGE                     = 42
    GROUP_CODE_START_WIDTH                      = 40
    GROUP_CODE_END_WIDTH                        = 41
    GROUP_CODE_THICKNESS                        = 39
    GROUP_CODE_SURFACE_TYPE                     = 75
    GROUP_CODE_SUREFACE_DENSITY_ROW_COUNT       = 73
    GROUP_CODE_SUREFACE_DENSITY_COLUMN_COUNT    = 74
    GROUP_CODE_ROW_COUNT                        = 71
    GROUP_CODE_COLUMN_COUNT                     = 72

    def __init__(self):
        self.follow = False
        self.parseVertex = False
        self.polyline = None
        self.vertex = None

    def startEntity(self):
        self.follow = False
        self.parseVertex = False
        self.polyline = None
        self.vertex = None

    def endEntity(self):
        pass

    def parseGroup(self, groupCode, value):
        if groupCode == self.GROUP_CODE_ENTITY_START:
            if value == self.ENTITY_VERTEX:
                # store the old vertex before
                if self.parseVertex:
                    self.polyline.addVertex(self.vertex)
                else:
                    self.parseVertex = True

                self.vertex = DXFVertex()

        elif groupCode == self.GROUP_CODE_START_X:
            if self.parseVertex:
                self.vertex.setX(value.getDouble())

        elif groupCode == self.GROUP_CODE_START_Y:
            if self.parseVertex:
                self.vertex.setY(value.getDouble())

        elif groupCode == self.GROUP_CODE_START_Z:
            if self.parseVertex:
                self.vertex.setZ(value.getDouble())

        elif groupCode == self.GROUP_CODE_START_WIDTH:
            if self.parseVertex:
                self.vertex.setStartWidth(value.getDouble())
            else:
                self.polyline.setStartWidh(value.getDouble())

        elif groupCode == self.GROUP_CODE_END_WIDTH:
            if self.parseVertex:
                self.vertex.setEndWidth(value.getDouble())
            else:
                self.polyline.setEndWidh(value.getDouble())

        elif groupCode == self.GROUP_CODE_THICKNESS:
            self.polyline.setThickness(value.getDouble())

        elif groupCode == self.GROUP_CODE_SURFACE_TYPE:
            self.polyline.setSurefaceType(value.getInt())

        elif groupCode == self.GROUP_CODE_ROW_COUNT:
            if self.parseVertex:
                self.vertex.setPolyFaceMeshVertex0(value.getInt())
            else:
                self.polyline.setRows(value.getInt())

        elif groupCode == self.GROUP_CODE_COLUMN_COUNT:
            if self.parseVertex:
                self.vertex.setPolyFaceMeshVertex1(value.getInt())
            else:
                self.polyline.setColumns(value.getInt())

        elif groupCode == self.GROUP_CODE_SUREFACE_DENSITY_ROW_COUNT:
            if self.parseVertex:
                self.vertex.setPolyFaceMeshVertex2(value.getInt())
            else:
                self.polyline.setSurefaceDensityRows(value.getInt())

        elif groupCode == self.GROUP_CODE_SUREFACE_DENSITY_COLUMN_COUNT:
            if self.parseVertex:
                self.vertex.setPolyFaceMeshVertex3(value.getInt())
            else:
                self.polyline.setSurefaceDensityColumns(value.getInt())

        else:
            if self.parseVertex:
                self.parseCommonProperty(groupCode, value, self.vertex)
            else:
                self.parseCommonProperty(groupCode, value, self.polyline)




