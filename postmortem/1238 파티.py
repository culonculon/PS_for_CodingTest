import sys
input = sys.stdin.readline

n,m,x = map(int, input().split())

# 무한대 값 표현
INF = int(1e9) 

# 주어지는 그래프 정보를 담는 N개 길이의 리스트 (1 부터 n 까지 활용)
graph = [[] for _ in range(n+1)]

for i in range(1, m+1):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

print(graph)

distance = [INF] * (n+1)
visited = [False] * (n+1)

def get_smallest_node():
    min_val = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            index = i
            
    return index

def dijstra(start):
    distance[start] = 0
    visited[start] = True

    for i in graph[start]:
        distance[i[0]] = i[1]
        
    for _ in range(n-1):
        next = get_smallest_node()
        visited[next] = True
        
        for j in graph[next]:
            if distance[next] + j[1] < distance[j[0]]:
                distance[j[0]] = distance[next] + j[1]
            

dijstra(x)
x_to_home = distance
print(x_to_home)

lst = []

print("x =", x)
print()
for i in range(1, n+1):
    distance = [INF] * (n+1)
    visited = [False] * (n+1)
    dijstra(i)
    print("distance =", distance)
    print("distance[x] =", distance[x])
    print("x_to_home[i] =", x_to_home[i])
    print()
    
    lst.append(distance[x] + x_to_home[i])
    
    
print(max(lst))
    
    