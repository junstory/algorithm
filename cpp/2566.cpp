#include <iostream>
using namespace std;

int main(void) {
	int m[9][9];
	int max = -1; //입력받는 수의 범위가 0~100 이므로 0보다 작은 값으로 초기화
	int col, row; // 최댓값의 행, 열 데이터를 담을 변수

	//값 입력 받기
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			cin >> m[i][j];
			//입력과 동시에 큰값일 경우 max, col, row에 저장
			//굳이 for문을 한 번 더 사용 안해도 됨!
			if (m[i][j] > max) {
				max = m[i][j];
				col = j+1; //index가 0부터 였으므로 1을 더해줌.
				row = i+1; //index가 0부터 였으므로 1을 더해줌.
			}
		}
	}
	//결과 출력
	cout << max << endl;
	cout << row << " " << col;

	return 0;
}