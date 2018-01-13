knn = KNearest()
training_data, responses = eval(open('data.txt', 'r').read())
training_data = np.array(training_data, np.float32)
responses = np.array(responses,np.float32)

knn.train(training_data,responses)

for single in master:
        if not np.sum(np.array(single, np.uint8)) == 0:
            single_testing = np.array(single, np.float32).reshape(1,256)
            ret, res, nei, dis = knn.find_nearest(single_testing, 3)
            res = int(res[0][0])
        else:
            res = 0
        print res
        imshow('img', np.array(single,npunit8).reshape((16,16)))
        waitKey(0)
        
