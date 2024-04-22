import sys

# _, 오른, 왼, 위, 아래
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

# 보드 크기, 말 개수
N, K = map(int, sys.stdin.readline().rstrip().split())

# 0:흰, 1:빨, 2:파
board = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(N)]

# 말 위치 기록(겹쳐진 말 포함)
record = [[[] for i in range(N)] for j in range(N)]

# 말 번호 별 위치, 방향 기록할 배열
horses_info = [[] for i in range(K+1)]
for i in range(1, K+1):
    row, culom, direction = map(int, sys.stdin.readline().split())
    horses_info[i] = [i, row-1, culom-1, direction]
    record[row-1][culom-1].append(i)
    
def is_bottom_horse(h_num, x, y):
    if record[x][y][0] == h_num:
        return True
    else:
        return False
    
def reverse_dir(direction):
    if direction == 1:
        return 2
    elif direction == 2:
        return 1
    elif direction == 3:
        return 4
    elif direction == 4:
        return 3


def is_blue_again(x, y, direction):
    rev_dir = reverse_dir(direction)
    nnx = x + dx[rev_dir]
    nny = y + dy[rev_dir]
    
    if nnx < 0 or nny < 0 or nnx >= N or nny >= N or board[nnx][nny] == 2:
        return True
    else: 
        return False


def move_next_pos(x, y, direction):
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 다음 칸이 파란 칸인경우
    if nx < 0 or nx >= N or ny <0 or ny>=N or board[nx][ny] == 2:
        # 또 벗어나거나 파란칸이며 이동 안하고 방향만 반대로
        if is_blue_again(nx, ny, direction):
            return x, y, reverse_dir(direction)
        else:
            rev_dir = reverse_dir(direction)
            return move_next_pos(x,y, rev_dir)
    
    # 다음 칸이 빨간칸인경우
    elif board[nx][ny] == 1:
        # 말 반대로 리버스
        rev_horses = record[x][y][::-1]
        
        for value in rev_horses:
            record[nx][ny].append(value)
            # 말들 정보 갱신
            hores_num, x, y, d = horses_info[value]
            horses_info[value] = [hores_num, nx, ny, d]                
            
        # 이전 칸에 있던 말들 모두 옮겼으니 빈칸으로 만들기
        record[x][y] = []
        
    # 다음 칸이 흰칸인경우    
    elif board[nx][ny] == 0:
        # 말들 차례로 다음 칸에 올림
        for value in record[x][y]:
            record[nx][ny].append(value)
            # 말들 정보 갱신
            hores_num, x, y, d = horses_info[value]
            horses_info[value] = [hores_num, x, y, d]

        # 이전 칸에 있던 말들 모두 옮겼으니 빈칸으로 만들기
        record[x][y] = []
    
    return nx, ny, direction


def move_all_horses():
    for hores in range(1, K+1):
        horse_num, row, colum, direction = horses_info[hores]
        if not is_bottom_horse(horse_num, row, colum):
            continue
        
        nx, ny, n_dir = move_next_pos(row, colum, direction)
        # 현재 말 정보 갱신
        horses_info[horse_num] = [horse_num, nx, ny, n_dir]
                   



def is_finish():
    for i in range(N):
        for j in range(N):
            if len(record[i][j]) >= 4:
                return True
    return False

# 게임 수행
answer = -1
time = 1
while time <= 10000:
    move_all_horses()

    if is_finish():
        answer = time
        break

    time += 1

print(answer)

