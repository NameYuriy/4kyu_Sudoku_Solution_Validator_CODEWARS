def valid_solution(board):
    rotated = tuple(zip(*board[::-1]))
    for i in range(0, 9):
        if sum(board[i])!=sum(rotated[i]) or sum(board[i])!=45:
            return False
    new_list=[]
    for q in range(3):
        for z in range(0, 7, 3):
            new_list.clear()
            for k in range(z, z+3):
                for j in range(0, 3):
                    new_list.append(board[k][j])
            if sum(new_list)!=45:
                return False
        board1 = [board[y][3:] for y in range(0, 9)]                           
    return True
