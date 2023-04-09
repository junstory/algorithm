#include <iostream>
#include <string>
using namespace std;

int main() {
	int N;
	int count = 1;
	string in_S="";
	cin >> N;
	cin >> in_S;
	for (int i = 0; i < N - 1; i++) {
		if ((int(in_S[i+1]) == int(in_S[i] - 1)) || (int(in_S[i+1]) == int(in_S[i] + 1))) {
			count++;
		}
		else {
			count = 1;
		}
		if (count >= 5) {
			break;
		}
		
	}

	if (count >= 5) {
		cout << "YES" << '\n';
	}
	else {
		cout << "NO" << '\n';
	}

	return 0;
}