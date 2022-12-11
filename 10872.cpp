#include <iostream>
using namespace std;

int Factorial(int num) {
	//N이 0인 경우 1반환
	if (num == 0) {
		return 1;
	}
	//1인 경우 더이상 진행 하지 않도록 1 반환.
	if (num == 1) {
		return 1;
	}
	else {
		return num * Factorial(num - 1);
	}
}

int main(void) {
	int N;
	//입력 및 출력
	cin >> N;
	cout << Factorial(N) << endl;

	return 0;
}