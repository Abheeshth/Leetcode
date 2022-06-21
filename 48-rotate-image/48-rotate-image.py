class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #first transpose
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        print(matrix)
        # try to swap the rows
        for i in range(m):
            matrix[i] = matrix[i][::-1]
        return matrix