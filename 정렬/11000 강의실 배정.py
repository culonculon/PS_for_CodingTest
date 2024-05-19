import sys
import heapq
input = sys.stdin.readline

N = int(input())

lecture = []

for i in range(N):
    lecture.append(list(map(int, input().split())))
    
print(lecture)

lecture = sorted(lecture, key = lambda x : (x[0], x[1]))

print(lecture)

heap = [lecture[0][1]]

print(heap)

for i in range(1, N):
    if heap[0] <= lecture[i][0]: # 특정 강의가 끝나는 시간이 다른 강의 시작 시간보다 이르다면 
        heapq.heappop(heap)
    heapq.heappush(heap, lecture[i][1])

print(heap)