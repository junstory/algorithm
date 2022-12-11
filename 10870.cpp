#include <iostream>
using namespace std;

int Fibonacci(int num) {
	//0번째와 1번째 항의 수는 자동으로 할 수 없는 부분 이므로 설정.
	if (num == 0) {
		return 0;
	}
	if (num == 1) {
		return 1;
	}
	//그 밖의 수들은 피보나치를 재귀로 구현하여 구함.
	else {
		return Fibonacci(num - 1) + Fibonacci(num - 2);
	}
}

int main(void) {
	int n;
	//입력 및 출력
	cin >> n;
	cout << Fibonacci(n) << endl;

	return 0;
}