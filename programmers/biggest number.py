def solution(numbers):
    answer = ''
    
    numbers.sort(key=lambda x: (str(x)*4)[:4], reverse=True)
    
    answer = ''.join([str(i) for i in numbers])
    
    return answer if answer[0] != '0' else '0'

# 시간 복잡도 O(nlogn)


# 다른사람 코드
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer


# 유형 : 그리디, 정렬