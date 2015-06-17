# -*- coding: utf-8 -*- 
#################################################  
# kmeans: k-means cluster  
# Date   : 2015-06-15  
# type   : main function
#################################################

from kmeans import kmeans,euclDistance,initCentroids,showCluster
from preprocess import preprocess,getLatLng
import sys
from numpy import*
import time  
import matplotlib.pyplot as plt
from time import sleep
import pickle

## step 1: load data  
print "step 1: load data..."     	
#dataSet, priceSet = preprocess(sys.argv[1])

#with open('data.txt', 'wb') as f:
    #pickle.dump(dataSet, f)

with open('data.txt', 'rb') as f:
    dataSet = pickle.load(f)

#with open('price.txt', 'wb') as f:
    #pickle.dump(priceSet, f)

with open('price.txt', 'rb') as f:
    priceSet = pickle.load(f)

##step 2: clustering...
averageSet = []
dataSet = mat(dataSet)
for k in range(1, 101):
    print k
    train = dataSet[:len(dataSet) / 2]
    test = dataSet[len(dataSet) / 2:]
    test_priceSet = priceSet[len(priceSet) / 2:]

    centroids, clusterAssment = kmeans(train, k)    

    # distinguish
    test_index = [-1] * len(test)
    for i in range(0, len(test)):
        min = -1
        for j in range(k):
            distance = euclDistance(centroids[j], test[i])
            if min == -1:
                min = distance
                test_index[i] = j
            elif distance < min:
                min = distance
                test_index[i] = j
        #print test_index[i]

    # calculate average price per class in train data
    total = [0] * k
    count = [0] * k
    for i in range(0, len(train)):
        index = int(clusterAssment[i, 0])
        total[index] = total[index] + priceSet[i]
        count[index] = count[index] + 1

    # average per class
    average = [0] * k
    for i in range(k):
        if count[i] != 0:
            average[i] = total[i] / count[i]
            #print average[i]

    # calculate error rate
    error = [0] * len(test)
    for i in range(k):
        for j in range(0, len(test)):
            if test_index[j] == i:
                #print test_priceSet[j]
                diff = fabs(test_priceSet[j] - average[i])
                diff_percent = (diff / test_priceSet[j]) * 100
                if diff_percent > 200:
                    diff_percent = 0

                #print 'diff %f ' % diff_percent
                error[j] = diff_percent
        #print 'average %s' % average[i]


    # calculus average error
    average_error = 0
    total_error = 0
    for e in error:
        total_error = total_error + e
    average_error = total_error / len(test)
    averageSet.append(average_error)
    print 'average error rate %f ' % average_error

#assert len(averageSet) == 100


plt.plot(range(1, 101), averageSet, marker='o', color='r')
plt.xlabel('K')
plt.ylabel('error rate %')
plt.show()

"""
plt.plot(range(0, len(test)), error, marker='o') 
plt.xlabel('')
plt.ylabel('error rate %')
#plt.ylim([0, 100])
plt.xlim([0, len(test)])
plt.show()
"""

## step 3: show the result  
#print "step 3: show the result..."  
#showCluster(dataSet, k, centroids, clusterAssment)  

