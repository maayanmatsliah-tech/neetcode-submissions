"""
understand:
- input: board (List containing 9 lists with 9 strs in each list.
         each str reps an int (1-9) or an empty slot (".").)
- output: bool repping:
            - whether each char in eah list is unique
            - whether all strs across lists at position i are unique
            - whether each str in a square is unique

plan:
- cols
    while i < 9:
        - i = 0 
        - new list = []
        - for list in lists:
            - append list[i] to new list if it doesn't = '.'
        - if new list != list(set(new list)) return false
        - i +=1        
- rows
    - for list in lists, remove periods 
    - if list(set(list)) != list return false
- squares
    - row_start = 0
    - row_end = 3
    - col_start = 0
    - col_end = 3

    - while col end 
    - square = []
    - while True:
        - for list in lists[row start: row end]
            - append list[col start: col end] to square
            - remove dots if necessary
            - if square list != list(set(square list)) return false
            - if col end != 9:
                - col start = col end
                - col end +=3
            elif row end!= 9:
                - row start = row end
                - row end +=3
                - col start = 0
                - col end = 3
            else:
                return True



"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for i in range(9):
            lst = [char for char in board[i] if char != '.' ]
            if len(lst) != len(set(lst)):
                return False
        
        # cols 
        for i in range(9):
            lst = []
            for l in board:
                if l[i] != '.':
                    lst.append(l[i])
            if len(lst) != len(set(lst)):
                return False
        
        #squares
        col_s = 0
        col_e = 3
        row_s = 0
        row_e = 3

        while True:
            lst = []
            for row in board[row_s:row_e]:
                for char in row[col_s:col_e]:
                    if char != '.':
                        lst.append(char)
            if len(lst) != len(set(lst)):
                return False
            if col_e < 9:
                col_s = col_e
                col_e +=3
            elif row_e < 9:
                col_s = 0
                col_e = 3
                row_s = row_e
                row_e +=3
            else:
                return True
         