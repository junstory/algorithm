#include <iostream>
using namespace std;

int a[1001] = { 0 };
int dp(int num) {
	if (a[num] > 0) return a[num];
	else {
		return a[num] = (dp(num - 1) + dp(num-2))%10007;
		
	}	
	
}

int main() {
	int n;
	cin >> n;
	a[1] = 1;
	a[2] = 2;
	cout << dp(n);

	return 0;
}