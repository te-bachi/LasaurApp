
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

import dxf_entity
import dxf_constants

from filereaders.dxf.util.point import Point


class DXFArc(dxf_entity.DXFEntity):

    def __init__(self):
        super(DXFArc, self).__init__()

        self.centerPoint = Point()
        self.radius = 0.0
        self.angleStart = 0.0
        self.angleEnd = 0.0
        self.counterclockwise = False


    def getType(self):
        return dxf_constants.DXFConstants.ENTITY_TYPE_ARC

    def getCenterPoint(self):
        return self.centerPoint

    def setRadius(self, radius):
        self.radius = radius

    def setAngleStart(self, angleStart):
        self.angleStart = angleStart

    def setAngleEnd(self, angleEnd):
        self.angleEnd = angleEnd

    def setCounterclockwise(self, counterclockwise):
        self.counterclockwise = counterclockwise

    def __repr__(self):
        return "centerPoint = [ " + str(self.centerPoint.getX()) + ", " + str(self.centerPoint.getY()) + ", " + str(self.centerPoint.getZ()) + \
               " ], radius = " + str(self.radius) + ", angleStart = " + str(self.angleStart) + ", angleEnd = " + str(self.angleEnd)