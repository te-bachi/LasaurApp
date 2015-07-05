
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

from nurbs import NURBS
from point import Point

class NURBSPointInterator(object):

    def __init__(self, nurbs, ntels):
        self.nurbs          = nurbs
        self.ntels          = ntels

        lenKnots            = len(self.nurbs.getKnots())
        lenControlPoints    = len(self.nurbs.getControlPoints())
        degree              = self.nurbs.getDegree()

        if lenKnots == degree + lenControlPoints + 1:
            self.lastInteral = lenKnots - degree - 1
            self.interval    = degree
        else:
            pass

    #private NURBS nurbs;
    #private int ntels;
    #private double dt = 0;
    #private double t = 0;
    #private int interval;
    #private int lastInterval;

    def __iter__(self):
        return self

    def next(self):
        pass
