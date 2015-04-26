
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

import dxf_entity
import dxf_constants


class DXFCircle(dxf_entity.DXFEntiy):

    def __init__(self):
        super(DXFCircle, self).__init__()

    def getType(self):
        return dxf_constants.DXFConstants.ENTITY_TYPE_CIRCLE
