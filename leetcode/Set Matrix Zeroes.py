class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        def setZero(x,y):
            #set column
            for i in range(m):
                matrix[i][y] = 0
            # set row:
            matrix[x] = [0 for _ in range(n)]
        dic = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0: dic.add((i,j))
        for x,y in dic:
            setZero(x,y)
