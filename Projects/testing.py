board = [
    [5,0,0,4,0,0,0,3,0],
    [0,0,0,0,1,0,6,0,0],
    [0,0,0,0,8,0,0,4,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,1,3,4,0,0,0,0],
    [0,7,3,2,0,0,0,0,9],
    [6,8,0,0,0,0,0,0,7],
    [0,0,0,5,0,0,0,2,0],
    [2,1,0,0,6,0,0,0,0]
]

def find_empty(bo):
    return None
  
def solve(bo):
    find = find_empty(bo)
    if not find:
    	print("Nothinf returned")
    else:
        row, col = find
        print(" returned")
solve(board)