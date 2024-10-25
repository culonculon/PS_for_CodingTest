def solution(board):
    Map = [[1] * len(board[0]) for i in range(len(board))]
    answer=[]
    
    bomb_idx=[]
    sides = [[0,0],[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]

    for idx_i, i in enumerate(board):
        for idx_j, j in enumerate(i):
            if j==1:
                bomb_idx.append([idx_i, idx_j])

    for b in bomb_idx:
        for s in sides:
            if 0<=(b[0]+s[0])<len(Map) and 0<=(b[1]+s[1])<len(Map[0]):
                Map[b[0]+s[0]][b[1]+s[1]]=0

    for i in Map:
        answer.extend(i)
    return sum(answer)