from ShapeDetector import ShapeDetector
import serial

def main(color, shape):
    notalign = True
    aligned = False
    ardunioData = serial.Serial('COM3', 9600)
    right = '0'
    left = '1'
    up = '2'
    down = '3'
    laser = '4'
    fire = '5'

    frame = ShapeDetector.FrameCapure(0)
    ShapeDetector.VideoRealease(0)
    while aligned == False:
        ShapeDetector.ColorShapeReader(color)
        image = ShapeDetector.ImagewColor(frame)
        coordinateX, coordinateY = ShapeDetector.ShapeDiscover(image,shape)
        centerX, centerY = ShapeDetector.FindCenterImage(image)
        distanceAway = ShapeDetector.DistanceTest(frame, shape)
        notalign = False
        if(centerY < coordinateY):
            notalign = True
            ardunioData.write(up.encode())
            #move up
        elif(centerY > coordinateY):
            notalign = True
            ardunioData.write(down.encode())
            #move down
        elif(centerX < coordinateX):
            notalign = True
            ardunioData.write(left.encode())
            #move left
        elif(centerX > coordinateX):
            notalign = True
            ardunioData.write(right.encode())
            #move right
        if(notalign == False):
            aligned = True
    #end while
    ardunioData.write(fire.encode())
    return 0

#do{
#   Color filter -
#   Detect Shape -
#   Find COM -
#   Find COS-
#   Move verticle if needed-
#   Move Horizontal if needed-
#}while(target.COM != COS)-
#Find distance
#Calculate needed angle
#Move to needed angle
#Fire






#if __name__ == "__main__":
    #main()






