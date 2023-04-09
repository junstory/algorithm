#include <iostream>
using namespace std;

char board[50][50];
int main() {
	int n, m;
	int min_B = 999;
	int min_W = 999;
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> board[i];
	}
	int B_count = 0;
	int W_count = 0;
	for (int i = 0; i < n-7; i++) {
		for (int j = 0; j < m-7; j++) {
			for (int a = i; a < i + 8; a++) {
				for (int b = j; b < j + 8; b++) {
					if ((a + b) % 2 == 0) {
						if (board[a][b] != 'B') {
							B_count++;
						}
					}
					else {
						if (board[a][b] != 'W') {
							B_count++;
						}
					}
				}
			}
			min_B = min(min_B, B_count);
			B_count = 0;
		}
	}
	for (int i = 0; i < n - 7; i++) {
		for (int j = 0; j < m - 7; j++) {
			for (int a = i; a < i + 8; a++) {
				for (int b = j; b < j + 8; b++) {
					if ((a + b) % 2 == 0) {
						if (board[a][b] != 'W') {
							W_count++;
						}
					}
					else {
						if (board[a][b] != 'B') {
							W_count++;
						}
					}
				}
			}
			min_W = min(min_W, W_count);
			W_count = 0;
		}
	}
	cout << min(min_B, min_W) << '\n';

	return 0;
}