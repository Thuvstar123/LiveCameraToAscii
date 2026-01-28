import cv2 as cv 
import time

class Frame:

    def __init__(self, frame):
        
        self.timeDelay = 0.1

        self.frame = frame

        self.asciiGrayscale = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"

        self.removeFromLeft = 0
        self.removeFromRight = -200
    
    def toGrayscale(self):

        self.frame = cv.cvtColor(self.frame, cv.COLOR_BGR2GRAY)

    def toList(self):

        self.frame = self.frame.tolist()
        
    def changeFPS(self, framesPerSecond):

        self.timeDelay = int(1 / framesPerSecond)

    def changeAsciiGrayScale(self, asciiGrayscale):
    
        self.asciiGrayscale = asciiGrayscale

    def lettersRemoved(self, startIndex, endIndex):
    
        self.removeFromLeft = startIndex
        self.removeFromRight = endIndex

    def returnFrameIfList(self):

        if isinstance(self.frame, list):

            return self.frame
        
        else:

            print("Error: Frame is not yet a list")
            return
        
    def delay(self):

        time.sleep(self.timeDelay)

    def printFrame(self):
        
        frame = self.frame

        for row in frame:

            line = ""
            
            for grayscaleValue in row:

                line += self.asciiGrayscale[grayscaleValue // 4]

            print(line[self.removeFromLeft : self.removeFromRight])
    
frameStream = cv.VideoCapture(0)

if not frameStream:

    print("Error: Cannot open camera")
    exit()

print()

while True:
    
    frameReadCorrectly, frame = frameStream.read()

    frame = Frame(frame)

    if not frameReadCorrectly:

        print("Error: Frame has not been successfully read")
        exit()
        break

    frame.toGrayscale()
    frame.toList()
    frame.delay()
    frame.printFrame()
    
    if cv.waitKey(1) == ord("q"):
        break