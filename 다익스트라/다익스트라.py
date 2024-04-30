import sys
input = sys.stdin.readline

# 무한대 값 표현
INF = int(1e9) 

# n : 노드의 개수 m : 간선의 개수
n, m = map(int, input().split()) 

# start 시작하는 노드의 숫자
start = int(input()) 

# 주어지는 그래프 정보를 담는 N개 길이의 리스트 (1 부터 n 까지 활용)
graph = [[] for _ in range(n+1)]

# 방문 처리 기록용
visited = [False] * (n+1) 

# 거리 테이블용
distance = [INF] * (n+1)

for _ in range(m):
    # a = 출발노드, b = 도착노드, c = 가중치
    a,b,c = map(int, input().split())
    graph[a].append((b, c))
    
def get_smallest_node():
    min_val = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_val and not visited[i] :  # 최소
            min_val = distance[i]
            index = i
        
    return index
    
    
def dijkstra(start):
    distance[start] = 0 # 시작 노드는 0으로 초기화
    visited[start] = True
    
    for i in graph[start]:
        distance[i[0]] = i[1]  # 시작노드와 연결된 노드의i[0] 거리 i[1] 입력 (inf -> w)
        
    print("distance = ", distance)
    
    print('graph =', graph)
    
    for _ in range(n-1):
        next = get_smallest_node()  # 거리가 구해진 노드 중 가장 짧은 거리 선택
        visited[next] = True        # 그 노드 방문처리
        
        for j in graph[next]:
            if distance[next] + j[1] < distance[j[0]]:
                distance[j[0]] = distance[next] + j[1]
        
        print("distance = ", distance)        

dijkstra(start)

'''
5 6
1
5 1 1
1 2 1
1 3 3
2 3 1
2 4 5
3 4 2
'''