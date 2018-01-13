from cv2 import *
import numpy as np

ind = 1
while ind<25:
    img = imread('Slide'+str(ind)+'.png')
    gr = 255 - cvtColor(img, COLOR_BGR2GRAY)
    _, bw = threshold(gr, 127, 255, THRESH_BINARY)
    contours, _ = findContours(bw.copy(), RETR_EXTERNAL, CHAIN_APPROX_SIMPLE)
    info = {}
    i = 0
    for cnt in contours:
        x, y, w, h = boundingRect(cnt)
        dig = bw[y:y+h, x:x+w]
        imshow('dig', dig)
        ch = waitKey(0)
        destroyWindow('dig')
        print chr(ch)
        res_dig = resize(dig, (16, 16)).ravel().tolist()
        print len(res_dig)
        info[i] = {'img':res_dig, 'tag':chr(ch)}
        i += 1
        
        
##    imshow('img', bw)
    f = open('Slide'+str(ind)+'.txt', 'w')
    f.write(str(info))
    f.close()
    ind += 1

    
waitKey(0)
destroyAllWindows()
