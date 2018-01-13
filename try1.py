from cv2 import *
import numpy as np

img = imread('Sudoku.png')

gr = 255 - cvtColor(img,COLOR_BGR2GRAY)
bw = threshold(gr, 127, 255,THRESH_BINARY)[1]

bw=resize(bw, (252,252))
s=28
##for i in range(9):
##    for j in range(9):
##        a=bw[i*9:(i+1)*9,j*9:(j+1)*9]
##        imshow('a',a)
##        waitKey(5000)
##for m in range(9):
##    for n in range(9):
##        imshow(b[n])

zz= bw.shape
print zz[-1]
imshow('bw',bw)
waitKey(0)
destroyAllWindows()
 
