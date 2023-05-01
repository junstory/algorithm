#include <iostream>
#include <string>
using namespace std;

void is_true(string temp) {
	for (int i = 0; i < temp.size() / 2; i++) {
		if (temp[i] != temp[temp.size()-1 - i]) {
			cout << "no" << '\n';
			return;
		}
	}
	cout << "yes\n";
	return;
}

int main() {
	string in_number;
	while (true) {
		cin >> in_number;
		if (in_number == "0") {
			break;
		}
		is_true(in_number);
	}

	return 0;
}