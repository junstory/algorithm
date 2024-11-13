#include <iostream>
using namespace std;

int main(void) {
	int x;
	cin >> x;
	int count = 0;
	
	//띠가 2부터 시작하기 때문에 sum은 2부터 시작
	for (int sum = 2; sum <= x; count++) {
		//벌집은 6각이므로 1을 기준으로 둘러싸는 벌집의 수는 6의 등비수열로 증가.
		//그 수가 원하는 x에 최대로 근접했을 때의 count 수가 이동하는 칸의 수. 
		sum += 6 * count;
	}
	
	if (x == 1) count = 1;
	
	cout << count;

	return 0;
}
