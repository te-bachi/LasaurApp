
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

import dxf_handler

#
#    0 -    9   String
#   10 -   39   Double precision 3D point value
#   40 -   59   Double-precision floating-point value
#   60 -   79   16-bit integer value
#   90 -   99   32-bit integer value
#  100          String
# 102           String
# 105           String
# 110-119       Double precision floating-point value
#
class DXFParser(dxf_handler.DXFHandler):

    GROUP_CODE_ENTITY_START     = 0
    GROUP_CODE_NAME             = 2
    SECTION_START               = "SECTION"
    SECTION_END                 = "ENDSEC"

    def __init__(self):
        from filereaders.dxf.dxf_constants                                  import DXFConstants
        from filereaders.dxf.parser.section.dxf_header_section_handler      import DXFHeaderSectionHandler
        from filereaders.dxf.parser.section.dxf_tables_section_handler      import DXFTablesSectionHandler
        from filereaders.dxf.parser.section.dxf_objects_section_handler     import DXFObjectsSectionHandler
        from filereaders.dxf.parser.section.dxf_entities_section_handler    import DXFEntitiesSectionHandler
        from filereaders.dxf.parser.entities.dxf_arc_handler                import DXFArcHandler
        from filereaders.dxf.parser.entities.dxf_circle_handler             import DXFCircleHandler
        from filereaders.dxf.parser.entities.dxf_line_handler               import DXFLineHandler
        from filereaders.dxf.parser.entities.dxf_polyline_handler           import DXFPolylineHandler
        from filereaders.dxf.parser.entities.dxf_lwpolyline_handler         import DXFLwpolylineHandler
        from filereaders.dxf.parser.entities.dxf_spline_handler             import DXFSplineHandler

        super(DXFParser, self).__init__()

        handler = DXFEntitiesSectionHandler(DXFConstants.SECTION_TYPE_ENTITIES)
        handler.addHandler(DXFArcHandler(DXFConstants.ENTITY_TYPE_ARC))
        handler.addHandler(DXFCircleHandler(DXFConstants.ENTITY_TYPE_CIRCLE))
        handler.addHandler(DXFLineHandler(DXFConstants.ENTITY_TYPE_LINE))
        handler.addHandler(DXFPolylineHandler(DXFConstants.ENTITY_TYPE_POLYLINE))
        handler.addHandler(DXFLwpolylineHandler(DXFConstants.ENTITY_TYPE_LWPOLYLINE))
        handler.addHandler(DXFSplineHandler(DXFConstants.ENTITY_TYPE_SPLINE))

        self.addHandler(handler)
        self.addHandler(DXFHeaderSectionHandler(DXFConstants.SECTION_TYPE_HEADER))
        self.addHandler(DXFObjectsSectionHandler(DXFConstants.SECTION_TYPE_OBJECTS))
        self.addHandler(DXFTablesSectionHandler(DXFConstants.SECTION_TYPE_TABLES))

        self.sectionStarts = False


    def parse(self, dxfstring):
        from dxf_group_buffer import DXFGroupBuffer
        from filereaders.dxf.dxf_document import DXFDocument

        linecount   = 0
        document    = DXFDocument()
        groupBuffer = DXFGroupBuffer(dxfstring)

        self.sectionStarts = False
        self.setDocument(document)

        for groupCode, value in groupBuffer:
            linecount += 1
            self.parseGroup(groupCode, value)

        print("Done")



    def parseGroup(self, groupCode, value):
        """
        :type  groupCode: int
        :type  value: filereaders.dxf.dxf_value.DXFValue
        """
        if groupCode == self.GROUP_CODE_ENTITY_START and value.getString() == self.SECTION_START:
            self.sectionStarts = True

        elif groupCode == self.GROUP_CODE_ENTITY_START and value.getString() == self.SECTION_END:
            self.handler = None
            self.parseIt = False

        elif groupCode == self.GROUP_CODE_NAME and self.sectionStarts:
            self.sectionStarts = False
            try:
                self.handler = self.handlers[value.getString()]
                self.handler.setDocument(self.document)
                self.handler.startSection()
                self.parseIt = True
            except KeyError:
                self.parseIt = False

        elif self.parseIt:
            #try:
                self.handler.parseGroup(groupCode, value)
            #except AttributeError:
            #    raise AttributeError()

