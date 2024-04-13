from itertools import combinations # 조합을 만들어주는 라이브러리

def solution(m, weights):
    answer = 0
    
    for i in range(1, len(weights)):
        for combi in combinations(weights, i): # 조합을 만든다.
            if sum(combi) == m:
                answer += 1
            
    return answer

# 완전탐색
# O(N*N)

# 다른사람 코드

def solution(m, weights):
    answer = search(m, weights, 0, 0)
    return answer

def search(m, weights, weight_sum, start): # start = 시작 위치
    if weight_sum == m:
        return 1
    elif weight_sum > m:
        return 0

    if start >= len(weights):
        return 0
    return search(m, weights, weight_sum+weights[start], start+1) + search(m, weights, weight_sum, start+1)


# 재귀