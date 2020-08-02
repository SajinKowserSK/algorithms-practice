# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 23:12:18 2020

# given stream of numbers where numbers can be added anytime, find sum of last K elements 

from models import *

def findKSum(stream, k):
    if k is None or stream is None or len(stream) == 0 or k == 0:
        return None
    
    q = regQueue()
    sumVal = 0 
    size = 0
    
    for x in range(0, len(stream)):
        q.enqueue(LinkedNode(stream[x]))
        sumVal += stream[x]
        size += 1
        
        if size == k:
            print(sumVal)
            result = q.dequeue()
            sumVal -= result.data
            size -= 1
    

            
findKSum([1,5,7,3,1], 2)
        
        
    
        
