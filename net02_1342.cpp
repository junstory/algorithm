#include <iostream>
#include <string>
using namespace std;

string s;
int result = 0;
int alpha[27];

void dfs(int idx, string cur) {
	if (idx == s.size()) {
		result++;
		return;
	}
	for (int i = 0; i < 26; i++) {
		if (alpha[i] == 0) continue;
		if (cur != "" && cur[cur.size() - 1] == (char)('a' + i)) continue;
		alpha[i]--;
		dfs(idx + 1, cur + (char)('a' + i));
		alpha[i]++;
	}
}

int main() {
	
	cin >> s;
	for (int i = 0; i < s.size(); i++){
		alpha[s[i] - 'a']++;
	}
	dfs(0, "");

	cout << result;
	return 0;
}