class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        newStart, newEnd = intervals[0]
        for start, end in intervals[1:]:
            if start <= newEnd:
                res.pop()
                newEnd = max(end, newEnd)
                res.append([newStart, newEnd])
            else:
                res.append([start, end])
                newStart, newEnd = start, end
        return res