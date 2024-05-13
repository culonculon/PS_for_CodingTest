# import sys
# input = sys.stdin.readline

# def visited(j, k, N):
#     for x in range(-2, 3):
#         for y in range(-2, 3):
#             if (abs(x)+abs(y) >= 3) or (j+x < 0 or j+x > N-1) or (k+y < 0 or k+y > N-1) :
#                 continue
#             available[j+x][k+y] = False

# def cost(j, k, N):
#     tmp = []
#     for x in range(-1,2):
#         for y in range(-1,2):
#             if (abs(x)+abs(y) >= 2):
#                 continue
#             tmp.append(maps[j+x][k+y])
    
#     # print("tmp =",tmp)
    
#     return sum(tmp)

# N = int(input())
# maps = []
# available = [[False if (j<1 or j>N-2 or i<1 or i>N-2) else True for j in range(N)] for i in range(N)]

# for i in range(N):
#     maps.append(list(map(int, input().split())))

# print(maps)

# print("availabe",available)

# for j in range(1, N-1):
#     for k in range(1, N-1):
#         if available[j][k]: 
#             visited(j,k,N)
#             c = cost(j,k,N)

import sys

def check(i, j, visited):
    for idx in range(4):
        next_i = i + d[idx][0]
        next_j = j + d[idx][1]
        if (next_i, next_j) in visited:
            return False
    return True

def dfs(visited, total):
    global answer
    if total >= answer:
        return
    if len(visited) == 15:
        answer = min(answer, total)
    else:
        for i in range(1, N-1):
            for j in range(1, N-1):
                if check(i,j,visited) and (i,j) not in visited:
                    tmp = [(i,j)]
                    tmp_cost = maps[i][j]
                    for idx in range(4):
                        next_i = i + d[idx][0]
                        next_j = j + d[idx][1]
                        tmp.append((next_i,next_j))
                        tmp_cost += maps[next_i][next_j]
                    dfs(visited + tmp, total + tmp_cost)

N = int(input())

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N = int(input())
answer = int(1e9)
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dfs([], 0)