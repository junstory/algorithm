#include <iostream>
using namespace std;

int main(void) {
	int nums[1000];
	int N, temp;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> temp;
		nums[i] = temp;
	}
	
	//선택정렬
	//제일 작은 값을 찾아서 맨 앞부터 차례대로으로 집어넣는다.
	int min;
	for (int i = 0; i < N; i++) {
		//min에 i의 인덱스를 넣고 i+1부터 N까지 비교하여 
		//가장 작은값을 i인덱스의 값으로 정해가며 정렬시킴
		min = i;
		for (int j = i + 1; j < N; j++) {
			if (nums[j] < nums[min]) {
				min = j;
			}
		}
		temp = nums[i];
		nums[i] = nums[min];
		nums[min] = temp;
	}

	for (int i = 0; i < N; i++) {
		cout << nums[i] << '\n';
	}


	return 0;
}

