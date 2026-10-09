# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def QS(pairs, s, e):
            if e - s <= 0:
                return 
            pivot = pairs[e]
            i, j = s, s
            while j < e:
                if pairs[j].key < pivot.key:
                    pairs[i], pairs[j] = pairs[j], pairs[i]
                    i += 1
                    j += 1
                else:
                    j += 1
            pairs[i], pairs[e] = pairs[e], pairs[i]
            
            QS(pairs, s, i-1)
            QS(pairs, i+1, e)

        QS(pairs, 0, len(pairs)-1)
        return pairs