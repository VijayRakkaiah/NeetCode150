class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import collections
        r = collections.defaultdict(set)
        c = collections.defaultdict(set)
        s = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                    
                if (val in r[row] or 
                    val in c[col] or 
                    val in s[(row // 3, col // 3)]):
                    return False

                r[row].add(val)
                c[col].add(val)
                s[(row // 3, col // 3)].add(val)

        return True

            

'''
36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''