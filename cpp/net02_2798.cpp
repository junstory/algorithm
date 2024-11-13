#include <iostream>
using namespace std;

int a[101];

int main() {
	int N, M;
	int n_max = 0;
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> a[i];
	}
	int sum = 0;
	for (int i = 0; i < N; i++) {
		for (int j = i + 1; j < N; j++) {
			for (int k = j + 1; k < N; k++) {
				sum = a[i]+a[j]+a[k];
				if (sum <= M) {
					n_max = max(sum, n_max);
				}
			}
		}
	}
	cout << n_max << '\n';

	return 0;
}