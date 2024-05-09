import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

dx = [0, -1, -1, -1, 0, 1, 1, 1] # 
dy = [-1, -1, 0, 1, 1, -1, 0, 1] 

H, W = map(int, input().split())

Distance = [[INF] * (W + 1) for _ in range(H + 1)]
Map = [[''] * (W + 1) for _ in range(H + 1)]
Q = []

# visited = [[False] * (H+1) for i in range(W+1)]

# print(D)
# print(M)
# print(visited)

# 시작 지점(K)와 목표 지점(*)의 좌표
py, px = 0, 0

for i in range(1, H+1):
    row = input().split()[0]
    for j in range(1, W+1):
        Map[i][j] = row[j-1]
        if Map[i][j] == 'K':
            Distance[i][j] = 0
            heapq.heappush(Q, (0,i,j))
            Sharp = (i,j)
        elif Map[i][j] == '*':
            py, px = (i,j)

while Q:
    a, b, c = heapq.heappop(Q) # 위치와 y,x 값
    if -a <= Distance[b][c]:
        for i in range(8):
            y = b + dy[i]
            x = c + dx[i]
            if 1 <= y <= H and 1<= x <= W and Map[y][x] != '#':
                d = (i < 5) - a
                if d < Distance[y][x]:
                    Distance[y][x] = d
                    heapq.heappush(Q, (-d, y, x))

print(Distance)
   
result = Distance[py][px] if Distance[py][px] < INF else -1


    
    
# print(Sharp)
# print(boat)



