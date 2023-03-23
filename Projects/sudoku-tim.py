# # # # Python Collections (Arrays)
# # # # There are four collection data types in the Python programming language:

# # # # List is a collection which is ordered and changeable. Allows duplicate members.
# # # # Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# # # # Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# # # # Dictionary is a collection which is ordered** and changeable. No duplicate members.
# # # # end" " - Stay on the same line while I keep printing things





# # Nested list:
# # creating list
# nestedList = [1, 2, ['a', 1], 3]
# # indexing list: the sublist has now been accessed
# # # # # # # # List = nestedList
# # # # # # # # subList = nestedList[2]
# # # # # # # # element = nestedList[2][0]
# # access the first element inside the inner list:
# element = nestedList[2][0]
# print("List inside the nested list: ", subList)
# print("First element of the sublist: ", element)





# # create matrix of size 4 x 3
# matrix = [[0, 1, 2],
#           [3, 4, 5],
#           [6, 7, 8],
#           [9, 10, 11]]

# rows = len(matrix)  # no of rows is no of sublists i.e. len of list (outer list)
# cols = len(matrix[0])  # no of cols is len of sublist (Inner list)
# print(rows, cols)
# # printing matrix
# print("matrix: ")
# for i in range(0, rows):
#     print(matrix[i])
# # accessing the element on row 2 and column 1 i.e. 3
# print("element on row 2 and column 1: ", matrix[1][0])
# # accessing the element on row 3 and column 2 i.e. 7
# print("element on row 3 and column 2: ", matrix[2][1])


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

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0
    return False

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col
    return None

print_board(board)
solve(board)
print("___________________")
print_board(board)