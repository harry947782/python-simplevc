'''
Created on 30 Aug 2014

@author: harry@alt-control.net
'''

from PIL import Image
import random,operator


def mult(tupl,scalar):
    return tuple(map(lambda x: scalar*x,tupl))

def add(tupl,scalar):
    return tuple(map(lambda x: x+scalar,tupl))

def positions(size):
    maxX,maxY = size
    for x in range(0,maxX):
        for y in range(0,maxY):
            yield (x,y)

   
def addtuple(a,b):
    return tuple(map(operator.add,a,b))

def padPositions(padCentre, padsize):
    for offset in positions((padsize,padsize)):
        yield addtuple(padCentre,add(offset,-1*int(padsize/2)))


def createKeyImage(size,padsize):
    keyIm = Image.new('LA', mult(size,padsize), (0xFF,0x00))
    for position in positions(size):
        padCentre = add(mult(position,padsize),int(padsize/2))
        for padPos in random.sample([x for x in padPositions(padCentre,padsize)],int(padsize*padsize/2)):
            keyIm.putpixel(padPos, (0x00,0xFF))
    return keyIm


def pixelSet(pixel):
    return pixel > 0x00


def invertPixel(cipherIm, pos):
    cipherIm.putpixel(pos,add(mult(cipherIm.getpixel(pos),-1),0xFF))


def createCipherImage(keyIm, plainIm, padsize):
    cipherIm = keyIm.copy()
    for position in positions(plainIm.size):
        padCentre = add(mult(position,padsize),int(padsize/2))
        if pixelSet(plainIm.getpixel(position)):
            for padPos in padPositions(padCentre,padsize):
                invertPixel(cipherIm,padPos)
    return cipherIm


if __name__ == '__main__':
    plainIm = Image.open("right.ppm").convert(mode='L')
    plainIm2 = Image.open("wrong.ppm").convert(mode='L')
    keyIm = createKeyImage(plainIm.size,4)
    keyIm.save("key.png","PNG")
    cipherIm = createCipherImage(keyIm,plainIm,4)
    cipherIm.save("right.png","PNG")
    falseCipherIm = createCipherImage(cipherIm,plainIm2,4)
    falseCipherIm.save("wrong.png","PNG")