#include <iostream>
#include <vector>
using namespace std;

int main() {
	int num, n;
	vector<int> nums;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> num;
		if (num == 0) {
			nums.pop_back();
		}
		else {
			nums.push_back(num);
		}
	}

	int sum = 0;
	for (auto elem : nums) {
		sum += elem;
	}
	cout << sum;

	

	return 0;
}