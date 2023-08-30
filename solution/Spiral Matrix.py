class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top, left = 0, 0
        bottom, right = len(matrix), len(matrix[0])
        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -=1
            if not (left < right and top < bottom):
                break
            for i in range(right - 1, left -1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1
            for i in range(bottom - 1, top -1, -1):
                res.append(matrix[i][left])
            left += 1
        return res