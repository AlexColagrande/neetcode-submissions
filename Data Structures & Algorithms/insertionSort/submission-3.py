# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if len(pairs) == 0:
            return []
        res = [pairs[:]]
        
        for i in range(1, len(pairs)):
            prev, cur = i-1, i
            while prev >= 0 and pairs[cur].key < pairs[prev].key:
                pairs[prev], pairs[cur] = pairs[cur], pairs[prev]
                prev -= 1
                cur -= 1
            res.append(pairs[:])
        
        return res
