### TikTok Round 1 Problem 2 
import heapq
def getMinCost(const, compatible1, compatible2, min_compatible):
  heap1 = heap2 = both = []
  bought = cost = 0
  for i in range(len(cost)):
     if compatible1[i] == 1 and compatible2[i] == 1:
        heapq.heappush(both, cost[i])
     elif compatible1[i] == 1:
       heapq.heappush(heap1, cost[i])
     elif compatble2[i] == 1:
       heapq.heappush(heap2, cost[i])
  if sum(i for i in compatible1 and i == 1) < min_compatible or sum(i for i in compatible2 and i ==1) < min_compatible:
     return -1
  
  while bought < min_compatible:
    if heap1[0] + heap2[0] >= both[0]:
      cost += both[0]
      heapq.heappop(both)
    else:
      cost += heap1[0] + heap2[0]
      heapq.heappop(heap1)
      heapq.heappop(heap2)
    bought += 1
  return cost