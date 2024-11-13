#include <iostream>
using namespace std;

int main(void) {
	int nums[5];
	int temp;
	int sum = 0;
	for (int i = 0; i < 5; i++) {
		cin >> temp;
		nums[i] = temp;
		sum += temp;
	}

	//버블정렬 자신의 왼쪽과 비교하여 나보다 크면 위치 바꿈.
	//큰 값이 맨 뒤에서부터 쌓이는 것이므로 j < 5-i 를 사용.
	for (int i = 0; i < 5; i++) {
		for (int j = 1; j < 5-i; j++) {
			if (nums[j - 1] > nums[j]) {
				temp = nums[j - 1];
				nums[j - 1] = nums[j];
				nums[j] = temp;
			}
		}
	}
	
	cout << sum / 5 << '\n';
	cout << nums[2] << endl;

	return 0;
}