import sys
input = sys.stdin.readline

N = int(input())


##에라토스테네스의 체##
array = [True for i in range(N + 1)]
lst = []

for i in range(2, int(N**1/2) + 1):
    if array[i] == True:
        j = 2
        while i * j <= N:
            array[i*j] = False
            j += 1

for i in range(2, N+1):
    if array[i]:
        # print(i, end=' ')
        lst.append(i)
##에라토스테네스의 체##

if (N - 4)%2 == 0:
    a,b = 2,2
    _N = N-4
else:
    a,b = 2,3
    _N = N-5

##골드바흐 추측##
for i in lst:
    if (_N-i) in lst:
        # print(i , N-i)
        break
##골드바흐 추측##

if N <= 7:
    print(-1)
else:
    print(a, b, i, _N-i)
