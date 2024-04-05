# 유형 비트마스킹, 구현

# your code goes here
import sys

S = set()
M = int(sys.stdin.readline())
all = set([i for i in range(1, 21)])
	
for cnt in range(M):
	i = list(sys.stdin.readline().split())
	cmd = i[0]
	x = i[1] if len(i) == 2 else 0

	if cmd == 'add':
		S.add(x)
	elif cmd == 'check':
		if x in S:
			print(1)
		else:
			print(0)
	elif cmd == 'remove':
		if x in S:
			S.remove(x)
	elif cmd == 'toggle':
		if x in S:
			S.remove(x)
		else:
			S.add(x)
	elif cmd == 'all':
		S.update(all)
	elif cmd == 'empty':
		S.clear()
  
  
#   다른사람 코드

import sys
input = sys.stdin.readline

bit = 0b0 # 2진수 활용

M = int(input())

for i in range(M):
    order = input().split()
    
    print(order, end =' ')
	
    if order[0] == 'add':
        bit |= (0b1 << int(order[1]))
    elif order[0] == 'remove':
        bit &= ~(0b1 << int(order[1]))
    elif order[0] == 'check':
        print(0b1 if bit & (0b1 << int(order[1])) != 0 else 0 , end=' ')
    elif order[0] == 'toggle':
        bit ^= (0b1 << int(order[1]))
    elif order[0] == 'empty':
        bit = 0b0
    elif order[0] == 'all':
        bit = 0b111111111111111111111
    
    print("bit =", bin(bit))
    
# ['add', '1'] bit = 0b10
# ['add', '2'] bit = 0b110
# ['check', '1'] 1 bit = 0b110
# ['check', '2'] 1 bit = 0b110
# ['check', '3'] 0 bit = 0b110
# ['remove', '2'] bit = 0b10
# ['check', '1'] 1 bit = 0b10
# ['check', '2'] 0 bit = 0b10
# ['toggle', '3'] bit = 0b1010
# ['check', '1'] 1 bit = 0b1010
# ['check', '2'] 0 bit = 0b1010
# ['check', '3'] 1 bit = 0b1010
# ['check', '4'] 0 bit = 0b1010
# ['all'] bit = 0b111111111111111111111
# ['check', '10'] 1 bit = 0b111111111111111111111
# ['check', '20'] 1 bit = 0b111111111111111111111
# ['toggle', '10'] bit = 0b111111111101111111111
# ['remove', '20'] bit = 0b11111111101111111111
# ['check', '10'] 0 bit = 0b11111111101111111111
# ['check', '20'] 0 bit = 0b11111111101111111111
# ['empty'] bit = 0b0
# ['check', '1'] 0 bit = 0b0
# ['toggle', '1'] bit = 0b10
# ['check', '1'] 1 bit = 0b10
# ['toggle', '1'] bit = 0b0
# ['check', '1'] 0 bit = 0b0


