
#this is a pretty weak example IMO, 
#but the more you think about it, the recursive requirements are satisfied
def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        print(numList[0])
        return numList[0] + listsum(numList[1:])

print(listsum([1,3,5,7,9]))


def dpMakeChange(coinValueList,change,minCoins):
   for cents in range(change+1):
      coinCount = cents
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
      minCoins[cents] = coinCount
   return minCoins[change]