#include <iostream>
#include <vector>
using namespace std;

int main(void) {
	int n, m, temp;
	cin >> n >> m;

	//벡터를 이용한 2차원 배열 초기화.
	vector<vector<int>> m1(n, vector<int>(m,0));
	vector<vector<int>> m2(n, vector<int>(m,0));

	//각 행렬 입력 받음.
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> temp;
			m1[i][j] = temp;
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> temp;
			m2[i][j] = temp;
		}
	}

	//더한 값을 그대로 출력.
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cout << m1[i][j]+m2[i][j] << ' ';
		}
		cout << endl;
	}

	return 0;
}