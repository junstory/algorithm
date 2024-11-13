#include <iostream>
using namespace std;

bool is_ok(int num) {
	int a[10] = { 0 };
	while (num != 0){
		a[num % 10]++;
		num /= 10;
	}
	for (int i = 0; i < 10; i++) {
		if (a[i] > 1) {
			return false;
		}
	}
	return true;
}

int main() {
	int N, M;
	int count = 0;
	while(cin >> N >> M) {
		for (int i = N; i <= M; i++) {
			if (is_ok(i)) {
				count++;
			}
		}
		cout << count << '\n';
		count = 0;
	}
	return 0;
}