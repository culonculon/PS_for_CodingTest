N = int(input())

t = N//9

lst = [[] for i in range(t)]

lst[0] = [1,2,3,4,5,6,7,8,9]

long_lst = [1,2,3,4,5,6,7,8,9]

for i in range(1, len(lst)):
    for j, num in enumerate(lst[i-1]):
        sum_next = sum(lst[i-1][0:j+1])
        lst[i].append(sum_next)
        long_lst.append(sum_next)
        
print(lst)
print(long_lst)

cnt = 1
while True:
    if cnt <= 10:
        cnt += 1
    else:
        ans = sum(long_lst[:N-10])
        if ans + 9 > N:
            print("ans =",ans)
            break
        
        