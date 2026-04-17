import sys
input = lambda:sys.stdin.readline().rstrip()

def is_valid_sudoku(board):
    row_dict = [{} for _ in range(9)]
    col_dict = [{} for _ in range(9)]
    box_dict = [{} for _ in range(9)]

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != '.':
                box_index = (i // 3) * 3 + j // 3
                row_dict[i][num] = row_dict[i].get(num, 0) + 1
                col_dict[j][num] = col_dict[j].get(num, 0) + 1
                box_dict[box_index][num] = box_dict[box_index].get(num, 0) + 1
                if row_dict[i][num] > 1 or col_dict[j][num] > 1 or box_dict[box_index][num] > 1:
                    return "INCORRECT"
    return "CORRECT"

for i in range(int(input())) :
    board = []
    M = 0
    while M < 9 :
        inp = input()
        if inp != "" :
            board.append(list(map(int, inp.split())))
            M += 1
    print(f"Case {i+1}:", is_valid_sudoku(board))