#include <iostream>
#include <vector>
using namespace std;

int main(void) {
	int N, temp;;
	vector<int> nums;
	cin >> N;
	
	//입력 받은 숫자를 1자리씩 vecotor에 추가합니다.
	while (N != 0) {
		nums.push_back(N % 10);
		N /= 10;
	}

	//버블 정렬을 이용하여 내림차순 정렬합니다.
	for (int i = 1; i < nums.size(); i++) {
		for (int j = 0; j < nums.size()-i; j++) {
			if (nums[j + 1] > nums[j]) {
				temp = nums[j];
				nums[j] = nums[j + 1];
				nums[j + 1] = temp;
			}
		}
	}
	
	//줄바꿈없이 출력후 마지막에 줄바꿈을 해줍니다.
	for (int i = 0; i < nums.size();i++) {
		cout << nums[i];
	}
	cout << '\n';

	return 0;
}
