def solution(d, budget):
    answer = 0

    for money in sorted(d):  # 각 부서별 예산 money
        budget -= money      # 총 남은 예산에서 부서별 예산 차감
        if budget >= 0 :
            answer += 1
        else:
            break
    
    return answer

# 시간 복잡도 O(nlogn)