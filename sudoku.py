class Solution:
    def getThreebyThree(self,board):
        newlist, newFirstlist, newSecondlist, newThirdlist = [], [], [], []
        for l in range(len(board)):
            for i in range(9):
                if i < 3:
                    newFirstlist.append(board[l][i])
                elif i < 6:
                    newSecondlist.append(board[l][i])
                else:
                    newThirdlist.append(board[l][i])
            if l % 3 == 2:
                newlist.append(newFirstlist)
                newlist.append(newSecondlist)
                newlist.append(newThirdlist)
                newFirstlist, newSecondlist, newThirdlist = [], [], []
        return newlist

    def getColumns(self, board):
        newBoard = []
        for i in range(9):
            newList = []
            for l in range(len(board)):
                newList.append(board[l][i])
            newBoard.append(newList)
        return newBoard

    def checkIfValid(self, board):
        for i in range(9):
            board[i].sort()
            for l in range(1, 9):
                if board[i][l] != '.' and board[i][l] == board[i][l - 1]:
                    return False
        return True

    def checkBoard(self, board):
        columnBoard = self.getColumns(board)
        threeByThreeBoard = self.getThreebyThree(board)
        boards = [board, columnBoard, threeByThreeBoard]
        for b in boards:
            if self.checkIfValid(b) == False:
                return False
        return True

input = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]

sol = Solution()
output = sol.checkBoard(input)
print(output)

