import sys
input = sys.stdin.readline

n = int(input())

computers = [[j for j in map(int, input().split()) ] for i in range(n)]

# 부모 테이블 초기화
parent = [0]*(n+1)
    
# 부모 테이블상에서 부모를 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

        
def find(x):
    if parent[x] != x:
        return find(parent[x])
    
    return x
    
def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, computers):
    answer = 0
    
    print(parent)
    
    # 간선 
    link = []
    
    for i, row in enumerate(computers):
        for j, computer in enumerate(row):
            # print("i,j = ", i, j)
            # print("row, col =", row, computer)
            if computer == 1:
                link.append((i+1, j+1))
                
    
    print(link)
    
    for i in link:
        union(i[0], i[1])
        
    print(parent)
    
    return answer


solution(n, computers)
