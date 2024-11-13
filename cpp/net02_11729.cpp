#include <iostream>
#include <cmath>
using namespace std;

//하노이
void hanoi(int n, int start, int to, int thru) {
	if (n == 1) {
		cout << start << " " << to << '\n';
	}
	else {
		hanoi(n-1, start, thru, to);
		cout << start << " " << to << '\n';
		hanoi(n - 1, thru, to, start);
	}
}
int main() {
	int n;
	cin >> n;
	cout << int(pow(2, n)) - 1 << '\n';
	hanoi(n,1,3,2);
	//일단3번째
	//안되면 2번째
	//없으면 3번째를 옆칸으로
	//첫칸이 없으면
	//2번째 칸에서 시도
	
	return 0;
}