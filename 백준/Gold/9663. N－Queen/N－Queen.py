n = int(input())

board = [ [0 for i in range(n)] for j in range(n) ]
queen_positions = [-1 for i in range(n)]
count = 0

def promising(row,col):
    for prev_row in range(row):
        if queen_positions[prev_row] == col or abs(prev_row - row) == abs(queen_positions[prev_row] - col):
            return False
    return True

def backtrack(row):
    global count
    if row == n:
        count += 1
        return
    for col in range(n):
        if promising(row,col):
            queen_positions[row] = col
            backtrack(row+1)
            queen_positions[row] = -1

backtrack(0)
print(count)
