class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        num_captures = 0
        row, column = self.findR(board)
        
        for i in range(column, 8):
            if(board[row][i] == "p"):
                num_captures += 1
                break
            elif(board[row][i] == "B"):
                break
        for i in range(column, -1, -1):
            if(board[row][i] == "p"):
                num_captures += 1
                break
            elif(board[row][i] == "B"):
                break
        for i in range(row, 8):
            if(board[i][column] == "p"):
                num_captures += 1
                break
            elif(board[i][column] == "B"):
                break
        for i in range(row, -1, -1):
            if(board[i][column] == "p"):
                num_captures += 1
                break
            elif(board[i][column] == "B"):
                break
                
        return num_captures
    
    def findR(self, board):
        num = 0
        for i in range(len(board)):
            if("R" in board[i]):
                num = board[i].index("R")
                break
        return i, num
