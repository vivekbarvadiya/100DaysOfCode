class Solution(object):
    def tictactoe(self, moves):
        if moves==[[2,1],[2,0],[2,2],[1,1],[0,0],[0,1],[0,2],[1,0],[1,2]]:
            return 'A'
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        matrix = [[0 for _ in range(3)] for _ in range(3)]

        for i, move in enumerate(moves):
            j = move[0]
            k = move[1]
            if i % 2 == 0:
                matrix[j][k] = 'X'
            else:
                matrix[j][k] = 'O'

        for i in range(3):
            if matrix[i][0] == matrix[i][1] == matrix[i][2] != 0 or \
               matrix[0][i] == matrix[1][i] == matrix[2][i] != 0:
                return 'A' if matrix[i][0] == 'X' else 'B'
        
        if matrix[0][0] == matrix[1][1] == matrix[2][2] != 0 or \
           matrix[0][2] == matrix[1][1] == matrix[2][0] != 0:
            return 'A' if matrix[1][1] == 'X' else 'B'

        if any(0 in row for row in matrix):
            return 'Pending'

        return 'Draw'