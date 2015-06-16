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
dataSet = preprocess(sys.argv[1])



##step 2: clustering...
dataSet = mat(dataSet) 
print dataSet
k = 10
centroids, clusterAssment = kmeans(dataSet, k)  





## step 3: show the result  
print "step 3: show the result..."  
showCluster(dataSet, k, centroids, clusterAssment)  

