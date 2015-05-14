
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

import dxf_entity
import dxf_constants


class DXFSpline(dxf_entity.DXFEntity):

    def __init__(self):
        super(DXFSpline, self).__init__()

        self.degree                 = 0
        self.controlPointsSize      = 0
        self.fitPointsSize          = 0
        self.nodePointsSize         = 0
        self.fitTolerance           = 0.0
        self.knotsTolerance         = 0.0
        self.controlPointTolerance  = 0.0
        self.splinePoints           = []

    def getType(self):
        return dxf_constants.DXFConstants.ENTITY_TYPE_SPLINE

    def setDegree(self, degree):
        self.degree = degree

    def setControlPointsSize(self, controlPointsSize):
        self.controlPointsSize = controlPointsSize

    def setFitPointsSize(self, fitPointsSize):
        self.fitPointsSize = fitPointsSize

    def setNodePointsSize(self, nodePointsSize):
        self.nodePointsSize = nodePointsSize

    def setFitTolerance(self, fitTolerance):
        self.fitTolerance = fitTolerance

    def setKnotsTolerance(self, knotsTolerance):
        self.knotsTolerance = knotsTolerance

    def setControlPointTolerance(self, controlPointTolerance):
        self.controlPointTolerance = controlPointTolerance

    def addSplinePoint(self, splinePoint):
        self.splinePoints.append(splinePoint)

