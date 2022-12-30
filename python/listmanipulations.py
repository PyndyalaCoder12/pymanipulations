import math
def objectMaxFrequency(list1):
    maxvalue = -math.inf
    for c in list1:
         if c > maxvalue:
             maxvalue = c
         else:
             continue
    return maxvalue
def certainFrequency(list1,value):
     frequencycount = 0
     for i in list1:
         if i == value:
             frequencycount += 1
         else:
             continue
     return frequencycount
def certainFrequencies(list1, listofvalues):
     frequencycount = 0
     for i in list1:
         if i in listofvalues:
             frequencycount += 1
         else:
             continue
     return frequencycount


    
