import cv2
from dbr import *
import sys
import os.path

def readBarcode(fileName):
    types = {
        0x3FFL: "OneD",
        0x1L  : "CODE_39",
        0x2L  : "CODE_128",
        0x4L  : "CODE_93",
        0x8L  : "CODABAR",
        0x10L : "ITF",
        0x20L : "EAN_13",
        0x40L : "EAN_8",
        0x80L : "UPC_A",
        0x100L: "UPC_E",
        0x200L: "INDUSTRIAL_25",
        0x2000000L: "PDF417",
        0x8000000L: "DATAMATRIX",
        0x4000000L: "QR_CODE"
    }

    initLicense("D426ABF246933C82A16D537FC46C064F")

    frame = cv2.imread(fileName, cv2.CV_LOAD_IMAGE_COLOR)

    results = decodeBuffer(frame)
    if (len(results) > 0):
        print "Total count: " + str(len(results))
        for result in results:
            print "Type: " + types[result[0]]
            print "Value: " + result[1] + "\n"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Please add a file path"
        sys.exit()

    fileName = sys.argv[1]
    if not os.path.isfile(fileName):
        print "File not found"
        sys.exit()

    print "OpenCV version: " + cv2.__version__
    readBarcode(fileName)
