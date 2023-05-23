#include <iostream>
using namespace std;

int a[10001][4] = {0};
int dp(int num) {
	if (a[num][1] > 0) {
		
	}
	else {
		a[num][1] = dp(num -1);
		a[num][2] = dp(num - 2);
		a[num][3] = dp(num - 3) + dp(num - 3) + dp(num - 3);
		return a[num][1] + a[num][2] + a[num][3];

	}

}

int main() {
	int n;
	cin >> n;
	
	a[1][1] = 1;
	a[2][1] = 1; a[2][2] = 1;
	a[3][1] = 1; a[3][2] = 1; a[3][3];
	for (int i = 4; i < 10001; i++) {
		a[i][1] = a[i-1][1];
		a[i][2] = a[i - 2][1] + a[i - 2][2];
		a[i][3] = a[i-3][1] + a[i-3][2] + a[i-3][3];
	}
	for (int i = 0; i < n; i++) {
		int temp;
		cin >> temp;
		cout << a[temp][1]+a[temp][2]+a[temp][3] << '\n';
	}

	return 0;
}