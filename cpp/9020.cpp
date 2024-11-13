#include <iostream>
#include <cmath>
using namespace std;

//인덱스를 숫자와 동일하게 하기 위해 1을 더함.
const int MAX = 100000 + 1;
//소수 여부를 가리기 위한 배열
int nums[MAX];

int main(void) {
	int t, n;
	int i = 0;

	//해당 인덱스에 해당 숫자를 담음.
	for (int i = 0; i < MAX; i++) {
		nums[i] = i;
	}

	//소수가 아니면 0으로 바꿈.
	nums[0] = nums[1] = 0;
	//j에 i*i를 담기 때문에 i*i<MAX라는 조건
	for (int i = 2; i * i < MAX; i++) {
		//k*i(k<i)까지는 소수 판별을 했으므로 i*i부터 시작
		for (int j = i * i; j < MAX; j += i) {
			if (nums[j] != 0) {
				nums[j] = 0;
			}
		}
	}


	//시행 횟수 변수 t
	cin >> t;
	for (int j = 0; j < t; j++) {
		cin >> n;
		//2로 나눈 값이 소수라면 제일 차가 적은 수 이므로
		//그 값을 출력 하고 다음 시행으로 넘어감.
		if (nums[n / 2] != 0) {
			cout << n / 2 << ' ' << n / 2 << '\n';
		}
		else {
			//두 수가 차이가 최소인 소수가 될 때 까지 i를 증가시킴
			while (1) {
				i++;
				if ((nums[n / 2 - i] != 0) && (nums[n / 2 + i] != 0)) {
					break;
				}
			}
			cout << n / 2 - i << ' ' << n / 2 + i << '\n';;
		}
		i = 0;
	}

	return 0;
}