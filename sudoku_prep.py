from cv2 import *
import numpy as np

img = imread('Sudoku.png')
gr = cvtColor(img, COLOR_BGR2GRAY)
edges = 255-threshold(gr, 127,255, THRESH_BINARY)[1]

lines = HoughLines(edges, 1, np.pi/180, 200)

print lines
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    line(img,(x1,y1),(x2,y2),(255,255,255),5)

gr = 255 - cvtColor(img,COLOR_BGR2GRAY)
bw = threshold(gr, 127, 255,THRESH_BINARY)[1]

contours = findContours(bw.copy(), RETR_EXTERNAL, CHAIN_APPROX_SIMPLE)[0]
print contours

for cnt in contours:
    x,y,w,h = boundingRect(cnt)
    rectangle(img, (x,y), (x+w,y+h), (0,255,0),1)
        
imshow('img',img)
bw=resize(bw, (252,252))
s=28
for i in range(9):
    for j in range(9):
        a=bw[i*s:(i+1)*s,j*s:(j+1)*s]
        imshow('a',a)
        waitKey(500)


imshow('bw',bw)
waitKey(0)
destroyAllWindows()

