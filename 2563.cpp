#include <iostream>
#include <vector>
using namespace std;

int main(void) {
	//벡터를 이용하여 100*100의 평면 생성
	vector<vector<int>> coord_p(100,vector<int>(100));
	int count = 0;
	int area = 0;
	int n, x, y;
	cin >> n;
	//좌표 평면을 굳이 1사분면으로 구현할 필요없이
	//색종이의 면적만을 알면 되므로 우하향일때 x,y가 증가한다고 생각.
	for (int i = 0; i < n; i++) {
		cin >> x >> y;
		//x,y의 시작점을 입력받으면 그 점부터 1씩 늘려가면서 색종이의 면적에 해당하는 위치의 값을 1 증가
		for (int j = 0; j < 10; j++) {
			for (int k = 0; k < 10; k++) {
				//인덱스는 0부터이므로 1을 빼줌.
				coord_p[x + j-1][y + k-1]++;
			}
		}
	}

	//색종이가 없는 영역은 숫자가 0, 색종이가 있는 영역은 1, 겹친 영역은 2이상이므로
	//0이 아니라면 색종이가 있는 것이므로 1씩 너비에 더함.
	//평면 모든 좌표에 대해 시행을 반복하면 색종이가 덮은 면적을 알 수 있음.
	for (int i = 0; i < 100; i++) {
		for (int j = 0; j < 100; j++) {
			if (coord_p[i][j] != 0) {
				area++;
			}
		}
	}
	cout << area << endl;
	return 0;
}