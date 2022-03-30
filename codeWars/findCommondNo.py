# find the most common number
from statistics import multimode

def highest_rank(arr):
    "hello = max(set(arr), key = arr.count)" #finds biggest number of deleted repeated element.
    return max(multimode((arr))) # if there are multiple modes it finds the bigger value

print(highest_rank([1,1,1,2,2,2]))