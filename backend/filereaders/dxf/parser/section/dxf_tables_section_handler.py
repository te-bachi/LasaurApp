
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

import dxf_section_handler


class DXFTablesSectionHandler(dxf_section_handler.DXFSectionHandler):

    GROUP_CODE_ENTITY_START         = 0
    GROUP_CODE_NAME                 = 2
    TABLE_START                     = "TABLE"
    TABLE_END                       = "ENDTAB"

    def __init__(self):
        from filereaders.dxf.dxf_constants import DXFConstants

        super(DXFTablesSectionHandler, self).__init__(DXFConstants.SECTION_TYPE_TABLES)

    def parseGroup(self, groupCode, value):
        if  groupCode == self.GROUP_CODE_ENTITY_START and value.getString == self.TABLE_START:
            return

        elif groupCode == self.GROUP_CODE_ENTITY_START and value.getString() == self.TABLE_END:
            if self.parseIt:
                pass

        elif groupCode == self.GROUP_CODE_NAME:

            try:
                self.handler = self.handlers[value.getString()]
                self.handler.setDocument(self.document)
                self.handler.startTable()
                self.parseIt = True
            except KeyError:
                self.parseIt = False

        elif self.parseIt and groupCode == self.GROUP_CODE_ENTITY_START and value.getString() == self.handler.getName():
            self.handler.parseGroup(groupCode, value)
