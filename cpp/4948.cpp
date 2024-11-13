#include <iostream>
#include <cmath>
using namespace std;

//인덱스를 숫자와 동일하게 하기 위해 1을 더함.
const int MAX = 2*123456 + 1;
//소수 여부를 가리기 위한 배열
int nums[MAX];

int main(void) {
	int n;
	int count = 0;

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
			if (nums[j] !=0) {
				nums[j] = 0;
			}
		}
	}

	//입력을 받아가며 n과 2n사이의 소수 개수 확인.
	while (1) {
		cin >> n;
		if (n == 0) {
			break;
		}

		//소수 배열을 이미 처리했기 때문에 읽어서 세기만 하면 됨.
		for (int i = n + 1; i <= 2 * n; i++) {
			if (nums[i] != 0) {
				count++;
			}
		}
		//개수 출력 후 count 0으로 초기화.
		cout << count << '\n';
		count = 0;
	}
	
	return 0;
}