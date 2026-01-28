import cv2 as cv
import time

frameStream = cv.VideoCapture(0)

if not frameStream:

    print("Error: Cannot open camera")
    exit()

print()

while True:
    
    time.sleep(0.1)
    frameReadCorrectly, frame = frameStream.read()


    if not frameReadCorrectly:

        print("Error: Frame has not been successfully read")
        exit()
        break

    
    grayscaleFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)   # Convert frame to Grayscale -> Simpler compute for ascii conversion

    asciiGrayScale = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"    # Ascii grayscale that we will use

    frameAsMatrix = grayscaleFrame.tolist()
    for row in frameAsMatrix:

        line = ""
        
        for grayscaleValue in row:

            line += asciiGrayScale[grayscaleValue // 4]

        print(line[ : -200])

    cv.imshow("frame", grayscaleFrame)
    
    if cv.waitKey(1) == ord("q"):
        break

frameStream.release()
cv.destroyAllWindows()