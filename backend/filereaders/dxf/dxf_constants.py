__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

import filereaders.dxf.util.vector

class DXFConstants:

    def __init__(self):
        pass

    DEFAULT_LAYER = "0"
    DEFAULT_X_AXIS_VECTOR = filereaders.dxf.util.vector.Vector(1.0, 0.0, 0.0)
    DEFAULT_Y_AXIS_VECTOR = filereaders.dxf.util.vector.Vector(0.0, 1.0, 0.0)
    DEFAULT_Z_AXIS_VECTOR = filereaders.dxf.util.vector.Vector(0.0, 0.0, 1.0)


    SECTION_START               = "SECTION"
    SECTION_END                 = "ENDSEC"

    SECTION_TYPE_BLOCKS         = "BLOCKS"
    SECTION_TYPE_CLASSES        = "CLASSES"
    SECTION_TYPE_ENTITIES       = "ENTITIES"
    SECTION_TYPE_HEADER         = "HEADER"
    SECTION_TYPE_OBJECTS        = "OBJECTS"
    SECTION_TYPE_TABLES         = "TABLES"
    SECTION_TYPE_THUMBNAILIMAGE = "THUMBNAILIMAGE"

    ENTITY_TYPE_ARC             = "ARC"
    ENTITY_TYPE_ATTRIB          = "ATTRIB"
    ENTITY_TYPE_BODY            = "BODY"
    ENTITY_TYPE_CIRCLE          = "CIRCLE"
    ENTITY_TYPE_DIMENSION       = "DIMENSION"
    ENTITY_TYPE_ELLIPSE         = "ELLIPSE"
    ENTITY_TYPE_HATCH           = "HATCH"
    ENTITY_TYPE_IMAGE           = "IMAGE"
    ENTITY_TYPE_INSERT          = "INSERT"
    ENTITY_TYPE_LEADER          = "LEADER"
    ENTITY_TYPE_LINE            = "LINE"
    ENTITY_TYPE_LWPOLYLINE      = "LWPOLYLINE"
    ENTITY_TYPE_MLINE           = "MLINE"
    ENTITY_TYPE_MTEXT           = "MTEXT"
    ENTITY_TYPE_POINT           = "POINT"
    ENTITY_TYPE_POLYLINE        = "POLYLINE"
    ENTITY_TYPE_RAY             = "RAY"
    ENTITY_TYPE_REGION          = "REGION"
    ENTITY_TYPE_SHAPE           = "SHAPE"
    ENTITY_TYPE_SOLID           = "SOLID"
    ENTITY_TYPE_SPLINE          = "SPLINE"
    ENTITY_TYPE_TABLE           = "TABLE"
    ENTITY_TYPE_TEXT            = "TEXT"
    ENTITY_TYPE_TOLERANCE       = "TOLERANCE"
    ENTITY_TYPE_TRACE           = "TRACE"
    ENTITY_TYPE_VERTEX          = "VERTEX"
    ENTITY_TYPE_VIEWPORT        = "VIEWPORT"
    ENTITY_TYPE_XLINE           = "XLINE"
