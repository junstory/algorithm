#include <iostream>
using namespace std;

//key point : 에라토스테네스의 체
//index와 수가 일치하도록 1000001의 배열 생성
const int MAX = 1000001;
int nums[MAX]={0};


int main(void) {
	int M, N;
	cin >> M >> N;
	
	
	//index 0은 필요하지 않고 1은 소수가 아니므로 -1로 지정
	nums[0] = nums[1] = -1;
	//2부터 1000001까지가 총 1000000개의 수 이므로 <=을 사용
	//i*i인 이유는 안에 for문에서 j=i*i이므로 오버플로우가 생기지 않도록 하기 위함.
	for (int i = 2; i * i <= MAX; i++) {
		//0이면 소수인 것으로 해당 수의 배수들을 모두 -1로 바꿈
		if (nums[i] == 0) {
			//이때 시작이 2*i가 아니라 i*i인 이유는
			//k(k<i)가 있을 때, i*k 까지는 소수가 아닌 수들이 -1로 '이미' 되었기 때문.
			//i*k 다음은 k+1 = i 이므로 i*i부터 i를 더해가며 -1로 바꾸어주면 됨.
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