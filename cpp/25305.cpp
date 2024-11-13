#include <iostream>
using namespace std;

int main(void) {
	int nums[1000];
	int N, k, temp;
	cin >> N >> k;
	for (int i = 0; i < N; i++) {
		cin >> temp;
		nums[i] = temp;
	}

	//삽입정렬
	//자신의 좌측은 모두 정렬되어 있다고 가정하고
	//좌측이 자신보다 크면 바꾸는 시행을 반복.
	//결과적으로 자신이 있어야하는 적절한 위치로 들어가면서 좌측이 계속해서 정렬된 상태 유지.
	//0은 정렬된 상태이므로 i는 1부터 시작.
	for (int i = 1; i < N; i++) {
		//i-1까지는 정렬이 된 상태이므로 j=i-1로 두고, 
		//정렬이 되지 않은 j+1을 비교하며 j+1항을 정렬시킴.
		for (int j = i-1; j >= 0; j--) {
			if (nums[j] > nums[j + 1]) {
				temp = nums[j];
				nums[j] = nums[j+1];
				nums[j+1] = temp;
			}
			else {
				break;
			}
		}
	}

	cout << nums[N - k] << '\n';

	return 0;
}
