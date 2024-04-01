import sys
sys.setrecursionlimit(10**6)  # 파이썬 순환 반복 횟수 제한 10**3 -> 10**6

def recursive(N):
    if N == 1:
        return 1
    if N == 0:
        return 0
    return recursive(N-1) + recursive(N-2)

def loop(N):
    Fn = [0,1]
    
    # FO = 0 (N=0) F1 = 1 (N=1,0) 예외 처리 
    while N > 0:
        Fn_1 = Fn[0] + Fn[1]
        Fn = [Fn[1], Fn_1]
        N -= 1
        
    return Fn[0]

def solution(x):
    answer = 0    
    answer = loop(x)%1234567
    
    return answer