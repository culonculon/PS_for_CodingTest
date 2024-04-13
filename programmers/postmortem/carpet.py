def solution(brown, red):
    answer = []
    carpet_size = brown + red # 갈색과 빨강의 합은 전체 카펫의 크기와 같다.    
    x = 3 # 가로 혹은 세로
    y = carpet_size//x # 세로 혹은 가로
    
    while True:
        if carpet_size%x != 0: # 카펫사이즈를 가로 혹은 세로로 나누면 나머지는 0 이어야 한다.
            x+=1
            y = carpet_size//x
            continue
        elif red != (x-2)*(y-2): # 빨간색 격자의 수는 (x-2)*(y-2)이 공식과 같다.
            x+=1
            y = carpet_size//x
            continue
        else:            
            answer = [max(x, y), min(x, y)] # 큰게 가로 작은게 세로
            break
            
    return answer

# 수학(소인수분해)
# 완전탑색
# 코드 시간복잡도 O(N)

# 다른사람 코드
def solution2(brown, red):
    for i in range(1, int(red**(1/2))+1): # red의 약수를 구하는법
        if red % i == 0:                  # i = x, red//i = y
            if 2*(i + red//i) == brown-4: # 공식 적용
                return [red//i+2, i+2]    # 공식 적용2 
