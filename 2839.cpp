#include <iostream>
using namespace std;

int main(void) {
	int n;
	int count = 0;
	cin >> n;
	if (n < 3) {
		return 0;
	}
	if (n % 5 >= 3 || n%5 == 0) {
		count += n / 5;
		if ((n % 5) % 3 != 0) {
			cout << -1 << endl;
			return 0;
		}
		count += (n % 5) / 3;
	}
	else {
		
		count += n / 3;
	}
	cout << count << endl;

	return 0;
}