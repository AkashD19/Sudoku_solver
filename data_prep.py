training_data = []
responses = []
from cv2 import *
import numpy as np

data = [eval(open('Slide'+str(i)+'.txt', 'r').read()) for i in range(1, 26)]

print len(data)

for q in range(10):
    for i in data:
        training_data.append([i[k]['img'] for k in i.keys() if i[k]['tag'] == str(q)][0])
        responses.append(q)
        img = resize(np.array(training_data[-1], np.uint8).reshape(16, 16), (80, 80))
        imshow('img', img)
        waitKey(10)
print responses

f = open("data.txt", "w")
f.write(str([training_data, responses]))
f.close()
