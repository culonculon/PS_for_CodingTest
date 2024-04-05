from collections import deque

def solution(progresses, speeds):
    answer = [] 

    # progresses와 speeds를 각각 queue로 변환
    progresses = deque([i for i in progresses]) 
    speeds = deque([i for i in speeds])
    
    while progresses:
        cnt = 0
        
        # 작업 진행
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        # 작업의 진행사항 확인
        for i in progresses:
            if i >= 100: 
                cnt += 1
            else:
                break
        
        if cnt > 0:
            answer.append(cnt)            

        # 완료된 작업 배포
        for i in range(cnt):
            progresses.popleft()
            speeds.popleft()
            
    return answer

# 시간 복잡도 O(n)