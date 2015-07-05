
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

from point import Point

class NURBS(object):

    def __init__(self, controlPoints, knots, weights, degree, closed):
        self.controlPoints  = controlPoints
        self.knots          = knots
        self.weights        = weights
        self.degree         = degree
        self.closed         = closed

    def getControlPoints(self):
        return self.controlPoints

    def setControlPoints(self, controlPoints):
        self.controlPoints = controlPoints

    def getKnots(self):
        return self.knots

    def setKnots(self, knots):
        self.knots = knots

    def getWeights(self):
        return self.weights

    def setWeights(self, weights):
        self.weights = weights

    def getDegree(self):
        return self.degree

    def setDegree(self, degree):
        self.degree = degree

    def isClosed(self):
        return self.closed

    def setClosed(self, closed):
        self.closed = closed

    def getBasicFunctions(self, i, u):
        # create empty lists with length (degree + 1)
        left    = [0.0] * (self.degree + 1)
        right   = [0.0] * (self.degree + 1)
        n       = [0.0] * (self.degree + 1)
        n[0]    = 1.0

        for j in range(1, self.degree + 1):
            left[j]     = u - self.knots[(i + 1) - j]
            right[j]    =     self.knots[i + j]         - u
            saved       = 0.0

            for r in range(0, j):
                t       = n[r] / (right[r + 1] + left[j - r])
                n[r]    = saved + (right[r + 1] * t)
                saved   = left[j - r] * t

            n[j] = saved

        return n

    def getPointAt(self, i, u):
        p = Point()
        n = self.getBasicFunctions(i, u)
        t = 0.0

        for j in range(0, self.degree + 1):
            d = i - self.degree + j
            w = self.weights[d]

            p.setX(p.getX() + (n[j] * self.controlPoints[d].getX() * w))
            p.setY(p.getY() + (n[j] * self.controlPoints[d].getY() * w))
            p.setZ(p.getZ() + (n[j] * self.controlPoints[d].getZ() * w))

            t += (n[j] * w)

        p.setX(p.getX() / t)
        p.setY(p.getY() / t)
        p.setZ(p.getZ() / t)

        return p

    def getPointAt(self, u):
        interval = self.findSpawnIndex(u)

        return self.getPointAt(interval, u)

    def findSpawnIndex(self, u):
        if u == self.knots[self.controlPoints.length + 1]:
            return self.controlPoints.length


        low  = self.degree
        high = self.controlPoints.length + 1
        mid  = (low + high) / 2

        while (u < self.knots[mid]) or (u >= self.knots[mid + 1]):
            if u < self.knots[mid]:
                high = mid
            else:
                low = mid

            mid = (low + high) / 2

        return mid

