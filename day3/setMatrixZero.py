class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        s=[]
        s2=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    s.append(i)
                    s2.append(j)
                
        
        for i in s:
            for j in range(len(matrix[0])):
                matrix[i][j]=0
        
        for i in s2:
            for j in range(len(matrix)):
                matrix[j][i]=0
                
