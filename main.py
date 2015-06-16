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
#dataSet = []    	
#fileIn=open(sys.argv[1])
#for line in fileIn.readlines():
	#lineArr=line.strip().split('\t')
	#try:
		#dataSet.append([float(lineArr[0]), float(lineArr[1])])
	#except ValueError:
		#print lineArr	
#print dataSet
dataSet, priceSet = preprocess(sys.argv[1])

with open('data.txt', 'wb') as f:
    pickle.dump(dataSet, f)

with open('data.txt', 'rb') as f:
    mylist = pickle.load(f)

print mylist 

with open('price.txt', 'wb') as f:
    pickle.dump(priceSet, f)

with open('price.txt', 'rb') as f:
    mylist = pickle.load(f)

print mylist 

##step 2: clustering...
dataSet = mat(dataSet)
k = 10
train = dataSet[:len(dataSet) / 2]
test = dataSet[len(dataSet) / 2:]
test_priceSet = priceSet[len(priceSet) / 2:]

centroids, clusterAssment = kmeans(train, k) 


test_index = []
for data in test:
    for j in range(k):
        min = -1
        distance = euclDistance(centroids[j], data)
        if min == -1:
            min = distance
            test_index[i] = j
        elif distance < min:
            min = distance
            test_index[i] = j
    print test_index[i]

# calculus average price per class in train data
# total price per class
total = [0] * k
for i in range(len(train)):
    index = clusterAssment[i, 0]
    total[index] = total[index] + priceSet[i]

# count per class
count = [0] * k
for item in clusterAssment:
    count[item[0]] = count[item[0]] + 1

print count

# average per class
average = [0] * k


total = 0
count = 0
for i in range(len(train)):
    if clusterAssment[i, 0] == index:
        total = total + priceSet[i]
        count = count + 1
print count
print total
price = total / count
print price

print test_priceSet[0]


## step 3: show the result  
#print "step 3: show the result..."  
#showCluster(dataSet, k, centroids, clusterAssment)  

