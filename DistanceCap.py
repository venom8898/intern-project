import cv2 as cv
import imutils

cap = cv.VideoCapture(0)

k = cv.waitKey(1)

if k%256 == 32:
    ret, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray, (5, 5), 0)
    edged = cv.Canny(gray, 35, 125)

    cnts = cv.findContours(edged.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    c = max(cnts, key=cv.contourArea)

    img = cv.minAreaRect(c)

cv.imshow('image', img)
cv.imwrite("Cap1.png",img)
cv.waitKey(0)