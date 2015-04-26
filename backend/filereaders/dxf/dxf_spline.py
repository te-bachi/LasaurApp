
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

import dxf_entity
import dxf_constants


class DXFSpline(dxf_entity.DXFEntiy):

    def __init__(self):
        super(DXFSpline, self).__init__()
        pass

    def getType(self):
        return dxf_constants.DXFConstants.ENTITY_TYPE_SPLINE
