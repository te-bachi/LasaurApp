
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

import filereaders.dxf.parser.section.dxf_section_handler

class DXFEntityHandler(filereaders.dxf.parser.section.dxf_section_handler.DXFSectionHandler):

    GROUP_CODE_ENTITY_START         = 0         # LINE, CIRCLE, ARC, ...
    GROUP_CODE_ELEMENT_REFERENCE    = 5
    GROUP_CODE_SOFT_POINTER         = 330
    GROUP_CODE_ENTITIES_FOLLOW      = 66        # Obsolete
    GROUP_CODE_SUBCLASS_MARKER      = 100       # AcDbEntity
    GROUP_CODE_START_X              = 10
    GROUP_CODE_START_Y              = 20
    GROUP_CODE_START_Z              = 30
    GROUP_CODE_END_X                = 11
    GROUP_CODE_END_Y                = 21
    GROUP_CODE_END_Z                = 31
    GROUP_CODE_LAYER_NAME           = 8
    GROUP_CODE_TRANSPARENCY         = 440
    GROUP_CODE_COLOR_CODE           = 62
    GROUP_CODE_COLORNAME            = 430
    GROUP_CODE_COLOR_24BIT          = 420
    GROUP_CODE_COLOR_TRANSPARENCY   = 440
    GROUP_CODE_FLAGS                = 70
    GROUP_CODE_EXTRUSION_X          = 210
    GROUP_CODE_EXTRUSION_Y          = 220
    GROUP_CODE_EXTRUSION_Z          = 230
    GROUP_CODE_VISIBILITY           = 60
    GROUP_CODE_LINE_TYPE            = 6
    GROUP_CODE_LINE_TYPE_SCALE      = 48
    GROUP_CODE_LINE_WEIGHT          = 370
    GROUP_CODE_THICKNESS            = 39
    GROUP_CODE_STYLENAME            = 3
    GROUP_CODE_TEXT                 = 1
    GROUP_CODE_ROTATION_ANGLE       = 50
    GROUP_CODE_MODELSPACE           = 67

    def __init__(self):
        from dxf_arc_handler import DXFArcHandler
        from dxf_circle_handler import DXFCircleHandler
        from dxf_line_handler import DXFLineHandler
        from dxf_polyline_handler import DXFPolylineHandler
        from dxf_lwpolyline_handler import DXFLwpolylineHandler
        from dxf_spline_handler import DXFSplineHandler

        self.entityHandler = None
        self.map = {
            DXFArcHandler.ENTITY_VALUE:         DXFArcHandler(),
            DXFCircleHandler.ENTITY_VALUE:      DXFCircleHandler(),
            DXFLineHandler.ENTITY_VALUE:        DXFLineHandler(),
            DXFPolylineHandler.ENTITY_VALUE:    DXFPolylineHandler(),
            DXFLwpolylineHandler.ENTITY_VALUE:  DXFLwpolylineHandler(),
            DXFSplineHandler.ENTITY_VALUE:      DXFSplineHandler()
        }

    def startEntity(self, value):
        try:
            self.entityHandler = self.map[value]
        except KeyError:
            pass

    def endEntity(self):
        self.entityHandler = None

    def parseGroup(self, groupCode, value):
        if  groupCode == self.GROUP_CODE_ENTITY_START and not self.entityHandler:
            self.startEntity(value)

        elif self.entityHandler:
            self.entityHandler.parseGroup(groupCode, value)

    def parseCommonProperty(self, groupCode, value, entity):
        if groupCode == self.GROUP_CODE_ELEMENT_REFERENCE:
            entity.setId(value.getString())

        if groupCode == self.GROUP_CODE_SOFT_POINTER:
            #entity.set...(value.getValue())
            pass

        elif groupCode == self.GROUP_CODE_LAYER_NAME:
            entity.setLayerName(value.getValue())

        elif groupCode == self.GROUP_CODE_FLAGS:
            entity.setFlags(value.getIntegerValue())

        elif groupCode == self.GROUP_CODE_VISIBILITY:
            entity.setVisibile(not value.getBooleanValue())

        elif groupCode == self.GROUP_CODE_LINE_TYPE:
            entity.setLineType(value.getValue())

        elif groupCode == self.GROUP_CODE_LINE_TYPE_SCALE:
            entity.setLineTypeScaleFactor(value.getDoubleValue())

        elif groupCode == self.GROUP_CODE_COLOR_CODE:
            entity.setColor(value.getIntegerValue())

        elif groupCode == self.GROUP_CODE_EXTRUSION_X:
            entity.setExtrusionX(value.getDoubleValue())

        elif groupCode == self.GROUP_CODE_EXTRUSION_Y:
            entity.setExtrusionY(value.getDoubleValue())

        elif groupCode == self.GROUP_CODE_EXTRUSION_Z:
            entity.setExtrusionZ(value.getDoubleValue())

        elif groupCode == self.GROUP_CODE_COLOR_24BIT:
            pass

        elif groupCode == self.GROUP_CODE_COLOR_TRANSPARENCY:
            pass

        elif groupCode == self.GROUP_CODE_LINE_WEIGHT:
            entity.setLineWeight(value.getIntegerValue())

        elif groupCode == self.GROUP_CODE_THICKNESS:
            entity.setThickness(value.getDoubleValue())

        elif groupCode == self.GROUP_CODE_MODELSPACE:
            entity.setModelSpace(value.getBooleanValue())


