#include <iostream>
#include <vector>
using namespace std;

int main(void) {
	//���͸� �̿��Ͽ� 100*100�� ��� ����
	vector<vector<int>> coord_p(100,vector<int>(100));
	int count = 0;
	int area = 0;
	int n, x, y;
	cin >> n;
	//��ǥ ����� ���� 1��и����� ������ �ʿ����
	//�������� �������� �˸� �ǹǷ� �������϶� x,y�� �����Ѵٰ� ����.
	for (int i = 0; i < n; i++) {
		cin >> x >> y;
		//x,y�� �������� �Է¹����� �� ������ 1�� �÷����鼭 �������� ������ �ش��ϴ� ��ġ�� ���� 1 ����
		for (int j = 0; j < 10; j++) {
			for (int k = 0; k < 10; k++) {
				//�ε����� 0�����̹Ƿ� 1�� ����.
				coord_p[x + j-1][y + k-1]++;
			}
		}
	}

	//�����̰� ���� ������ ���ڰ� 0, �����̰� �ִ� ������ 1, ��ģ ������ 2�̻��̹Ƿ�
	//0�� �ƴ϶�� �����̰� �ִ� ���̹Ƿ� 1�� �ʺ� ����.
	//��� ��� ��ǥ�� ���� ������ �ݺ��ϸ� �����̰� ���� ������ �� �� ����.
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