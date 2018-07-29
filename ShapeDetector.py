import cv2 as cv
import imutils
from PIL import Image
import math


class ShapeDetector:

    global H_High
    global H_Low
    global S_High
    global S_Low
    global V_High
    global V_Low

    def DistanceTest(ImgCap, shape):

        KNOWN_DISTANCE = 24.0

        if (shape == "rectangle"):
            #load rectangle image
            img = cv.imread("")
            KNOWN_WIDTH = ...
            marker = ShapeDetector.find_marker(img)
        elif (shape == "square"):
            # load square image
            img = cv.imread("")
            KNOWN_WIDTH = ...
            marker = ShapeDetector.find_marker(img)
        elif (shape == "triangle"):
            # load triangle image
            img = cv.imread("")
            KNOWN_WIDTH = ...
            marker = ShapeDetector.find_marker(img)
        elif (shape == "pentagon"):
            # load pentagon image
            img = cv.imread("")
            KNOWN_WIDTH = ...
            marker = ShapeDetector.find_marker(img)
        elif (shape == "star"):
            # load star image
            img = cv.imread("")
            KNOWN_WIDTH = ...
            marker = ShapeDetector.find_marker(img)

        focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH

        marker = ShapeDetector.find_marker(ImgCap)

        inches = ShapeDetector.distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])

        return inches

    def find_marker(image, shape):
        # convert the image to grayscale, blur it, and detect edges
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        gray = cv.GaussianBlur(gray, (5, 5), 0)
        edged = cv.Canny(gray, 35, 125)

        # find the contours in the edged image and keep the largest one;
        # we'll assume that this is our piece of paper in the image
        cnts = cv.findContours(edged.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        c = max(cnts, key=cv.contourArea)

        # compute the bounding box of the of the paper region and return it
        return cv.minAreaRect(c)

    def distance_to_camera(knownWidth, focalLength, perWidth):
        # compute and return the distance from the maker to the camera
        return (knownWidth * focalLength) / perWidth

    def ImagewLines(ImgCap):#draws lines from the color binary to be used in shape reconition
        grad_x = cv.Sobel(ImgCap, cv.CV_16S, 1, 0, ksize=3, scale=1, delta=0, borderType=cv.BORDER_DEFAULT)
        grad_y = cv.Sobel(ImgCap, cv.CV_16S, 0, 1, ksize=3, scale=1, delta=0, borderType=cv.BORDER_DEFAULT)

        abs_grad_x = cv.convertScaleAbs(grad_x)
        abs_grad_y = cv.convertScaleAbs(grad_y)

        grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

        cnts = cv.findContours(grad.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        c = max(cnts, key=cv.contourArea)
        #cv.imshow("image", c)
        return c

    def ShapeDiscover(ImageCap, shape):

        resized = imutils.resize(ImageCap, width= 300)
        ratio = ImageCap.shape[0] / float(resized.shape[0])

        contours = cv.findContours(resized, cv.RETR_EXTERNAL , cv.CHAIN_APPROX_SIMPLE)

        contours = contours[0] if imutils.is_cv2() else contours[1]

        for c in contours:
            shapeName = "Unidentified"
            perimeter = cv.arcLength(c, True)
            approx = cv.approxPolyDP(c, 0.04 * perimeter, True)

            if len(approx) == 3:
                shapeName = "triangle"

            elif len(approx) == 4:
                (x, y, l, h) = cv.boundingRect(approx)
                ar = l / float(h)

                if ar >= 0.95 and ar <= 1.05:
                    shapeName = "square"
                else:
                    shapeName = "rectangle"

            elif len(approx) == 5:
                shapeName = "pentagon"

            elif len(approx) == 10:
                shapeName = "star"

            else:
                shapeName = "circle"

            if (shape == shapeName):

                M = cv.moments(c)
                cX = int((M["m10"] / M["m00"]) * ratio)
                cY = int((M["m01"] / M["m00"]) * ratio)

                c = c.astype("float")
                c *= ratio
                c = c.astype("int")
                #cv.drawContours(ImageCap, [c], -1, (0, 255, 0), 1)

                return cX, cY

            #cv.putText(image, shape, (cX, cY), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

            #print(shape)

        #cv.imshow("Image", image)
        #key = cv.waitKey(0)
        #if key == ord('q') or key == 27:
            #cv.destroyAllWindows()
            #print("Exiting")
            #break

    def FrameCapure(self):
        cap = cv.VideoCapture(0)
        ret, frame = cap.read()
        if frame is None:
            print("No camera found")
        cap.release()


        return frame

    def ColorShapeReader(color):
        S_High = 255
        S_Low = 102
        V_High = 255
        V_Low = 51
        if color.lower() == 'red':
            H_High = 13
            H_Low = 0
        elif color.lower() == 'blue':
            H_High = 115
            H_Low = 46
        elif color.lower() == 'green':
            H_High = 95
            H_Low = 30
            S_High = 167
            S_Low = 51
            V_High = 174
            V_Low = 52
        elif color.lower() == 'yellow':
            H_High = 41
            H_Low = 26
        elif color.lower() == 'purple':
            H_High = 139
            H_Low = 107
            S_High = 255
            S_Low = 54
            V_High = 235
            V_Low = 46

    def ImagewColor(frame):  # filters colors and then uses the gaussian blur to help with errors
        frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        frame_threshold = cv.inRange(frame_HSV, (H_Low, S_Low, V_Low), (H_High, S_High, V_High))
        frame_blur = cv.GaussianBlur(frame_threshold, (5, 5), 0)
        return frame_blur

    def FindCenterImage(cap):
        image = Image.open(cap)
        width, height = image.size

        centerY = height / 2;
        centerX = width / 2;

        return centerX, centerY

    def AdjustTarget(distance):
        heightDiff = 0
        initalVelocity = 10.15
        gravity = 9.8
        distance = distance * 0.3048

        angle = math.atan((2*initalVelocity*heightDiff)/ (gravity * distance))
        #transition angle to times we have to go up
        writetime = (angle * 10)/ 45
        return writetime


