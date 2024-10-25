import sys
input = sys.stdin.readline

def dfs(graph,start,visit):
    ans_dfs.append(start)  # 방문 노드 추가
    visit[start] = 1       # 방문 표시
    
    for n in graph[start]:
        if not visit[n]:   # 방문하지 않은 노드인 경우
            dfs(graph,n, visit)
    

def bfs(graph,start):
    visited = []
    queue = [start]
                
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)

    print(visited)

N, M, V = map(int, input().split())
    
graph = [[] for i in range(N+1)]
visit = [0]*(N+1)
ans_dfs = []

for i in range(1, N+1):
    f,l = map(int, input().split())
    graph[f].append(l)
    graph[l].append(f)

for i in range(1, N+1):
    graph[i].sort()


dfs(graph, V, visit)
print(ans_dfs)
bfs(graph, V)

