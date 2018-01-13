from cv2 import *
import numpy as np

img = imread('Slide22.png')
gr = 255 - cvtColor(img, COLOR_BGR2GRAY)
_, bw = threshold(gr, 127, 255, THRESH_BINARY)
bw1 = bw.copy()
satisfied = False
while not satisfied:
    bw = dilate(bw, np.ones((5, 5), np.uint8))
    bw = erode(bw, np.ones((3, 3), np.uint8))
    imshow('bw', bw)
    if waitKey(0) == 27:
        satisfied = True
        
contours, _ = findContours(bw.copy(), RETR_EXTERNAL, CHAIN_APPROX_SIMPLE)
info = {}
i = 0
for cnt in contours:
    x, y, w, h = boundingRect(cnt)
    dig = bw1[y:y+h, x:x+w]
    imshow('dig', dig)
    ch = waitKey(0)
    destroyWindow('dig')
    print chr(ch)
    res_dig = resize(dig, (16, 16)).ravel().tolist()
    print len(res_dig)
    info[i] = {'img':res_dig, 'tag':chr(ch)}
    i += 1
    
    
imshow('img', bw)
##print info
f = open('Slide22.txt', 'w')
f.write(str(info))
f.close()
waitKey(0)
destroyAllWindows()
