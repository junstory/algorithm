#include <iostream>
using namespace std;

//key point : 에라토스테네스의 체
//index와 수가 일치하도록 1000001의 배열 생성
const int MAX = 1000001;
int nums[MAX]={0};


int main(void) {
	int M, N;
	cin >> M >> N;
	
	//각 배열에 해당하는 숫자 입력
	
	nums[0] = nums[1] = -1;
	for (int i = 2; i * i <= MAX; i++) {
		if (nums[i] == 0) {
			for (int j = i * i; j < MAX; j += i) {
				if (nums[j] == 0) {
					nums[j] = -1;
				}
			}
		}
	}
	for (int i = M; i <= N; i++) {
		if (nums[i]==0) {
			cout << i << '\n';
		}
	}

	return 0;
}