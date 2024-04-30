import sys
arr = list()
# 줄어드는 수는 최대 9876543210까지 있으므로 0부터 9까지 백트래킹을 활용하여 줄어드는 수들을 전부 만들어 준다.

result = set()  # 모든 줄어드는 수를 전부 담는다.

def dfs():
    if len(arr) > 0:
        result.add(int("".join(map(str, arr))))
        
    for i in range(0, 10): # 여기서 0~9의 숫자를 통해 조합을 만든다. 단, 줄어드는 수 여야 한다.
        if len(arr) == 0 or arr[-1] > i: # 마지막 값이 더 큰 경우
            arr.append(i)
            dfs()
            arr.pop()

N = int(sys.stdin.readline())

try:
    dfs()
    result = list(result)
    result.sort()
    print(result)
    print(result[N - 1])
except:
    print(-1)
    

# 조합으로도 풀이 가능