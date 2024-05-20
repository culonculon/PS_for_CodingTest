import sys
import heapq
input = sys.stdin.readline

N = int(input())

lecture = []

for i in range(N):
    lecture.append(list(map(int, input().split())))
    
lecture = sorted(lecture, key = lambda x : (x[0], x[1]))

heap = [lecture[0][1]]

for i in range(1, N):
    if heap[0] <= lecture[i][0]: # 현재 강의의 시작 시간이 가장 먼저 끝나는 강의의 종료 시간보다 늦거나 같으면
        heapq.heappop(heap) # 가장 빨리 끝나는 강의를 힙에서 제거합니다.
    heapq.heappush(heap, lecture[i][1]) # 현재 강의의 종료 시간을 힙에 추가합니다.