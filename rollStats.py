from random import *

def rollStats():
    stats = []
    for i in range(6):
        tempList = []
        for roll in range(4):
            tempList.append(randint(1,6))
        tempList.remove(min(tempList))
        stats.append(sum(tempList))
    return stats