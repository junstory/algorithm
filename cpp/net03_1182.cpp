#include <iostream>
using namespace std;

int a[20];
int N, S;

int N_count = 0;

void dfs(int idx, int s) {
	if (idx == N)return;
	if (s + a[idx] == S) {
		N_count++; return;
	}
	dfs(idx + 1, s);
	dfs(idx + 1, s + a[idx]);
}

int main() {
	
	cin >> N, S;

	if (N == 1) {
		if (N == S) {
			cout << 1;
			return 0;
		}
		else {
			cout << 0;
			return 0;
		}
	}
	for (int i = 0; i < N; i++) {
		cin >> a[i];
	}

	dfs(0, 0);
	cout << N_count;
	return 0;
}