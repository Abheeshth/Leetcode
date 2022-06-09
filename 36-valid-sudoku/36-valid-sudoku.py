class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        m = len(board[0])
        
        
        def find(board,row,col,c):
            # check row
            #print(row)
            for i in range(9):

                if board[i][col] == c and i != row :
                    print('aya1')
                    return False
                if board[row][i] == c and i != col:
                    print('aya2')
                    return False
                if board[3*(row//3)+i//3][3*(col//3)+i%3] == c and 3*(row//3)+i//3 != row and 3*(col//3)+i%3 != col :
                    
                    print('aya3')
                    return False
            return True  
        
        
        for i in range(n):
            for j in range(m):
                if board[i][j]!= '.':
                    if find(board,i,j,str(board[i][j])) == False:
                        return False
        return True
    
    '''    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boardMap = collections.defaultdict(list)
        for x in range(9):
            for y in range(9):
                char = board[x][y]
                if char != '.': 
                    if char in boardMap:
                        for pos in boardMap[char]:
                            if (pos[0]== x) or (pos[1] == y) or (pos[0]//3 == x//3 and pos[1]//3 == y//3):
                                return False
                    boardMap[char].append((x,y))
   
        return True'''
            
        