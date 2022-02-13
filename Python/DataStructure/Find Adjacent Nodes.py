# https://edabit.com/challenge/3DAkZHv2LZjgqWbvW

def is_adjacent(matrix, node1, node2):
    found = False
    if matrix[node1][node2] == 1:
        found = True
    return found


matrix = [[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]]
print(is_adjacent(matrix, 0, 1))
print(is_adjacent(matrix, 0, 2))
print(is_adjacent(matrix, 2, 1))
print("")
matrix1 = [[0, 1, 0, 1, 1], [1, 0, 1, 0, 0], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [1, 0, 0, 1, 0]]
print(is_adjacent(matrix1, 0, 3))
print(is_adjacent(matrix1, 1, 4))
print(is_adjacent(matrix1, 3, 2))

'''
matrix = [[0,1,0,0],[1,0,1,1],[0,1,0,1],[0,1,1,0]]
is_adjacent(matrix, 0, 1), True)
is_adjacent(matrix, 0, 2), False)
is_adjacent(matrix, 2, 1), True)

matrix = [[0,1,0,1,1], [1,0,1,0,0],[0,1,0,1,0],[1,0,1,0,1],[1,0,0,1,0]]
is_adjacent(matrix, 0, 3), True)
is_adjacent(matrix, 1, 4), False)
is_adjacent(matrix, 3, 2), True)
'''
