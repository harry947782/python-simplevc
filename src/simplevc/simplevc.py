'''
Created on 30 Aug 2014

@author: harry <AT> alt-control.net
'''

from PIL import Image
import random, operator

# the second value is the ALPHA, setting it to transparent for blank pixels allows the images to be overlayed in software
BLANKPIXEL = 0xFF, 0x00
FILLEDPIXEL = 0x00, 0xFF

def mult(tupl, scalar):
    return tuple(map(lambda x: scalar * x, tupl))

def add(tupl, scalar):
    return tuple(map(lambda x: x + scalar, tupl))

def allPositions(size):
    maxX, maxY = size
    for x in range(0, maxX):
        for y in range(0, maxY):
            yield (x, y)

def addtuple(a, b):
    return tuple(map(operator.add, a, b))

def allZeroCentrePositions(size):
    halfX = int(size[0] / 2)
    halfY = int(size[1] / 2)
    for x in range(-1*halfX, halfX):
        for y in range(-1*halfY, halfY):
            yield (x, y)

def padPositions(padCentrePoint, padSize):
    for offset in allZeroCentrePositions((padSize, padSize)):
        yield addtuple(padCentrePoint, offset)

def randomHalfOf(vals):
    return random.sample(vals, int(len(vals) / 2))

def generateKeySetPositions(size, padsize):
    for position in allPositions(size):
        getPadCentre = add(mult(position, padsize), int(padsize / 2))
        allPadPositions = list(padPositions(getPadCentre, padsize))
        for padPos in randomHalfOf(allPadPositions):
            yield padPos

def createKeyImage(size, padsize):
    keyIm = Image.new('LA', mult(size, padsize), BLANKPIXEL)
    for pos in generateKeySetPositions(size, padsize):
        keyIm.putpixel(pos, FILLEDPIXEL)
    return keyIm

def isPixelSet(pixelValue):
    return pixelValue > 0x00

def invertPixel(cipherIm, pos):
    cipherIm.putpixel(pos, add(mult(cipherIm.getpixel(pos), -1), 0xFF))

def invertPad(cipherIm, padCentre, padSize):
    for padPos in padPositions(padCentre, padSize):
        invertPixel(cipherIm, padPos)

def getSetPixels(image):
    for position in allPositions(image.size):
        if isPixelSet(image.getpixel(position)):
            yield position

def getPadCentre(position, padSize):
    return add(mult(position, padSize), int(padSize / 2))

def createCipherImage(keyIm, plainIm, padSize):
    assert keyIm.size == mult(plainIm.size, padSize)
    assert plainIm.mode == 'L'
    assert keyIm.mode == 'LA'
    cipherIm = keyIm.copy()
    for position in getSetPixels(plainIm):
        padCentre = getPadCentre(position, padSize)
        invertPad(cipherIm, padCentre, padSize)
    return cipherIm


if __name__ == '__main__':
    plainIm = Image.open("cubs.ppm").convert(mode='L')
    keyIm = createKeyImage(plainIm.size, 2)
    keyIm.save("key.png", "PNG")
    cipherIm = createCipherImage(keyIm, plainIm, 2)
    cipherIm.save("right.png", "PNG")

