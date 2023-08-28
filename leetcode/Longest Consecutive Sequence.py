class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mindic = {

        }
        maxdic = {

        }
        dis = collections.Counter(nums).keys()
        for i in dis:
            if i + 1 in mindic and i - 1 in maxdic:
                newMin = maxdic[i-1]
                newMax = mindic[i+1]
                mindic[newMin] = newMax
                maxdic[newMax] = newMin
                del mindic[i+1]
                del maxdic[i-1]
            elif i + 1 in mindic:
                newMax = mindic[i+1]
                maxdic[newMax] = i
                mindic[i] = newMax
                del mindic[i+1]
            elif i - 1 in maxdic:
                newMin = maxdic[i-1]
                maxdic[i] = newMin
                mindic[newMin] = i
                del maxdic[i-1]
            else:
                mindic[i] = i
                maxdic[i] = i
            # print(i, mindic, maxdic)
        res = 0
        # print(mindic)
        for i in mindic:
            res = max(res, mindic[i] - i + 1)
        return res