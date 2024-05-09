# import sys
# import heapq
# input = sys.stdin.readline

result = '9'*80

def back_T(good, N):    
    if len(good) > 1:
        for i in range((len(good)//2) + 1):
            if good[-i:] == good[-i*2:-i]:
                return ''
    
    if len(good) == N:
        global result
        result = min(good, result)
        return
    
    a = back_T(good + '1', N)
    b = back_T(good + '2', N)
    c = back_T(good + '3', N)

N = int(input())

for i in range(1, 4):
    good = str(i)
    s = back_T(good, N)

print(result)


def check(num):
    length = len(num)
    for idx in range(1, length//2 + 1):
        if num[-idx:] == num[-(idx*2):-idx]:
            return False
    else:
        return True

def recursive(num):
    global N, res
    if len(num) == N:
        print(num)
        exit()
    for i in '123':
        if check(num + str(i)):
            recursive(num + str(i))
    return

N = int(input())
recursive('1')