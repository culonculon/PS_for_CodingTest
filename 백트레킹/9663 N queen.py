# import sys
# input = sys.stdin.readline

# def is_promising(map, num, after):
#     for i in range(num):
#         if abs(num - i) == abs(after - map[i]) or map[i] == after:
#             return False
        
#     return True
    
# def dfs(map, num):
#     if num == N:
#         global cnt
#         cnt += 1
#         return
    
#     for i in range(N):
#         if is_promising(map, num, i):
#             map.append(i)
#             dfs(map, num+1)
#             map.pop()
            
# N = int(input())
# cnt = 0
# dfs([], 0)
# print(cnt)


# 

def get_possibles(positions, size):
    i = len(positions)
    
    for j in range(size):
        valid = True
        for x, y in positions:
            if x == i or y == j or i-j == x-y or size-i-1-j == size-x-1-y:
                valid = False
                break
            if valid:
                yield(i, j)


def get_count(positions, left, size):
    if left == 0:
        print(positions)
        return 1
    
    result = 0
    
    for possible in get_possibles(positions, size):
        result += get_count(positions + (possible ,), left-1, size, possible[0])
        
        return result
    
def main(size):
    return get_count(tuple(), size, size)
    


print(main(10))
