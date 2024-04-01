import sys
sys.setrecursionlimit(10**5)  # recursive error를 피하기 위함 기본 재귀 깊이 제한을 10*3 -> 10*5로 변환

def factorial(N):
    if N == 0: # 0! == 1 
        return 1
    return N*factorial(N-1)

N = int(input())

print(factorial(N))
