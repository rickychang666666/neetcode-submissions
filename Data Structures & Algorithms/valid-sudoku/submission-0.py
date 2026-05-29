class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #case 1 check row
        for i in range(9):
            seen = set()
            for j in range(9):
                tmp = board[i][j]
                if tmp != ".":
                    if tmp in seen:
                        return False
                    seen.add(tmp)
        
        #case 2 check column
        for i in range(9):
            seen = set()
            for j in range(9):
                tmp = board[j][i]
                if tmp != ".":
                    if tmp in seen:
                        return False
                    seen.add(tmp)
        
        #case 3 check box
        for i in range(0,9,3):
            for j in range(0,9,3):
                seen = set()
                for bi in range(i,i+3):
                    for bj in range(j,j+3):
                        tmp = board[bi][bj]
                        if tmp != ".":
                            if tmp in seen:
                                return False
                            seen.add(tmp)
        return True