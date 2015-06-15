#################################################  
# kmeans: k-means cluster  
# Author : roberthuang  
# Date   : 2015-06-15  
# type   : main function
#################################################


from kmeans import kmeans,euclDistance,initCentroids,showCluster
import sys
from numpy import*
import time  
import matplotlib.pyplot as plt



	
## step 1: load data  
print "step 1: load data..."     	
dataSet = []    	
fileIn=open(sys.argv[1])
for line in fileIn.readlines():
	lineArr=line.strip().split('\t')
	try:
		dataSet.append([float(lineArr[0]), float(lineArr[1])])
	except ValueError:
		print lineArr	
#print dataSet








##step 2: clustering...
dataSet = mat(dataSet) 
#print dataSet
k=4
centroids, clusterAssment =kmeans(dataSet, k)  


## step 3: show the result  
print "step 3: show the result..."  
showCluster(dataSet, k, centroids, clusterAssment)  
