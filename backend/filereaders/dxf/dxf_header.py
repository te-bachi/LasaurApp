
__author__ = 'Andreas Bachmann <andreas.bachmann@fablabwinti.ch>'


class DXFHeader:

    #
    MAINTENACE_VERSION      = (  70, "$ACADMAINTVER" )          # Maintenance version number
    VERSION                 = (   1, "$ACADVER" )               # The AutoCAD drawing database version number
    ANGLE_BASE              = (  50, "$ACADVER" )               # Angle 0 direction
    ANGLE_DIRECTION         = (  70, "$ANGDIR" )                # Angle direction
                                                                #   1 = Clockwise angles,
                                                                #   0 = Counterclockwise angles

    VERSION_STR = {
        "MC0.0":            "AutoCAD Version 1.0",
        "AC1.2":            "AutoCAD Version 1.2",
        "AC1.40":           "AutoCAD Version 1.40",
        "AC1.50":           "AutoCAD Version 1.50",
        "AC2.10":           "AutoCAD Version 2.10",

        "AC2.21":           "AutoCAD Version 2.21",
        "AC2.22":           "AutoCAD Version 2.22",
        "AC1001":           "AutoCAD Version 2.22",
        "AC1002":           "AutoCAD Version 2.50",
        "AC1003":           "AutoCAD Version 2.60",
        "AC1004":           "AutoCAD Release 9",
        "AC1005":           "AutoCAD Pre-release 10",
        "AC1006":           "AutoCAD Release 10",
        "AC1007":           "AutoCAD Pre-release 11",
        "AC1008":           "AutoCAD Pre-release 11b",
        "AC1009":           "AutoCAD Release 11",
        "AC1010":           "AutoCAD Pre-release 13a",
        "AC1011":           "AutoCAD Pre-release 13b",
        "AC1012":           "AutoCAD Release 13",
        "AC1013":           "AutoCAD Pre-release 14",
        "AC1014":           "AutoCAD Release 14/14.01"
    }

    def __init__(self):
        self.bla = "a"

