#include <iostream>
using namespace std;



int a[128][128];
int n;
int blue = 0;
int white = 0;

void sol(int x, int y, int size) {
	bool is_B = true;
	bool is_W = true;
	for (int i = x; i < x+size; i++) {
		for (int j = y; j < y + size; j++) {
			if (a[i][j] == 1) is_W = false;
			if (a[i][j] == 0) is_B = false;
		}
	}
	if (is_W) {
		white++;
		return;
	}
	if (is_B) {
		blue++;
		return;
	}
	sol(x, y, size / 2);
	sol(x + size / 2, y, size / 2);
	sol(x, y + size / 2, size / 2);
	sol(x + size / 2, y + size / 2, size / 2);

}

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> a[i][j];
		}
	}

	sol(0,0,n);
	cout << white << '\n' << blue;
	return 0;
}