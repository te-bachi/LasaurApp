__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'

class DXFEntity:

    def __init__(self, id = "", document = None):
        """

        :param id:
        :param document:
        :type id: str
        :type document: filereaders.dxf.dxf_document.DXFDocument
        """
        self.id = id
        self.document = document
        self.layerName = ""
        self.flags = 0
        self.visibility = True
        self.lineType = ""
        self.lineTypeScaleFactor = 1.0
        self.color = 0
        self.lineWeight = 0
        self.thickness = 0.0
        self.modelSpace = True

    def setId(self, id):
        self.id = id

    def setDocument(self, document):
        self.document = document

    def setLayerName(self, layerName):
        self.layerName = layerName

    def setFlags(self, flags):
        self.flags = flags

    def setVisibile(self, visibility):
        self.visibility = visibility

    def setLineType(self, lineType):
        self.lineType = lineType

    def setLineTypeScaleFactor(self, lineTypeScaleFactor):
        self.lineTypeScaleFactor = lineTypeScaleFactor

    def setColor(self, color):
        self.color = color

    def setExtrusionX(self, extrusionX):
        pass

    def setExtrusionY(self, extrusionY):
        pass

    def setExtrusionZ(self, extrusionZ):
        pass

    def setLineWeight(self, lineWeight):
        self.lineWeight = lineWeight

    def setThickness(self, thickness):
        self.thickness = thickness

    def setModelSpace(self, modelSpace):
        self.modelSpace = modelSpace
