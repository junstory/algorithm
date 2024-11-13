#include <iostream>
#include <vector>
using namespace std;

int main(void) {
	//정수의 개수 input, 입력받는 정수 temp, 원하는 숫자의 개수 count
	int input, temp;
	int count = 0;
	cin >> input;
	//벡터를 이용하여 정수형 벡터 선언.
	vector<int> num(input);
	//input만큼 숫자를 입력 받음.
	for (int i = 0; i < input; i++) {
		cin >> temp;
		num[i] = temp;
	}

	//원하는 숫자 입력 후 개수 확인 및 출력
	cin >> temp;
	for (int i = 0; i < input; i++) {
		if (num[i] == temp) {
			count++;
		}
	}
	cout << count;

	return 0;
}