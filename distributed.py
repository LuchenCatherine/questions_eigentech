#################################################  
# distributed k-means cluster    
# Date   : 2017-12-30
# pseudocode
#################################################  
  
from numpy import *  
import time  
import matplotlib.pyplot as plt  
  
  
# calculate Euclidean distance  
def euclDistance(vector1, vector2):  
    return (sum(power(vector2 - vector1, 2)))  
  
# init centroids with random samples  
def initCentroids(dataSet, k):      

#init clusterAssment
def initAssment():
    for every machine:
        clusterAssment = mat(zeros(size))

# process data in every machine
def distributed_kmeans_1(dataSet):
    global clusterAssment
    global centroids
    numSamples = dataSet.shape[0]
    k = centroids.shape[0] 
    # store part of the weights corresponding to the data in this machine
    clusterPart = mat(zeros((k, n)))
    clusterCnt = mat(zeros((k,1)))
    # find the centroid who is closest
    for i in range(numSamples):
        minDist = 9999999
        minIndex = 0
        for j in range(k):
            distance = euclDistance(centroids[j,:], dataSet[i,:])
            if distance < minDist:
                minDist = distance
                minIndex = j
        clusterPart[minIndex,:] += dataSet[i,:]
        clusterCnt[minIndex] += 1
        
        if clusterAssment[i] != minIndex:
            clusterAssment[i] = minIndex
    return clusterPart, clusterCnt

# process important data in a central way
def distributed_kmeans_2(k):
    part = mat(zeros((k, n)))
    cnt = mat(zeros((k,1)))
    #accumulate the weight and the number of points belongs to each centroid
    for every machine with dataSet:
        clusterPart, clusterCnt = distributed_kmeans_1(dataSet)
        part += clusterPart
        cnt += clusterCnt
    centroids = divide(part, cnt)

def run():
    global centroids
    global clusterAssment
    global k = constant1        # centroids number
    global n = constant2        # dimensions
    global m = constant3        # number of samples 
    centroids = initCentroids(k)
    clusterAssment = initAssment(m)
    

    while(True):
        tmp = centroids
        distributed_kmeans_2(k)
        #convergence
        if(euclDistance(tmp, centroids) < episilon):
            break
        ################
