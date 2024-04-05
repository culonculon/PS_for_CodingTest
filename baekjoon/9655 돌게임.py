# 유형 DP, math

import sys

N = int(sys.stdin.readline())

print("SK" if N%2 == 1 else "CY")


# 다른사람 코드

#include <iostream>
#include <algorithm>
# using namespace std;

# int main() {
# 	int N;           // 돌의 개수
# 	int DP[1000];    // 게임과정의 횟수

# 	cin >> N;

# 	DP[0] = 0;
# 	DP[1] = 1;
# 	DP[2] = 2;

# 	for (int i = 3; i <= N; i++) {
# 		DP[i] = min(DP[i - 1] + 1, DP[i - 3] + 1);
# 	}

# 	// 게임 과정 횟수의 홀짝에 따라 승패 결정
# 	if (DP[N] % 2 == 1) {
# 		cout << "SK";
# 	}
# 	else {
# 		cout << "CY";
# 	}

# 	return 0;
# }
# 출처: https://beginnerdeveloper-lit.tistory.com/83 [초보 개발자의 이야기, 릿허브:티스토리]