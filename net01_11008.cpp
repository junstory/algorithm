#include <iostream>
#include <string>
using namespace std;



int main() {
	int T;
	int time = 0;
	int idx = 0;
	string in_S, paste;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> in_S >> paste;
		while(idx < in_S.size()) {
			if (idx + paste.size()-1 < in_S.size()) {
				if (in_S.substr(idx,paste.size()) == paste) {
					idx += paste.size();
				}
				else {
					idx++;
				}
			}
			else {
				idx++;
			}
			time++;
			
		}
		cout << time << '\n';
		time = 0;
		idx = 0;
	}

	return 0;
}