#include <iostream>
#include <queue>
using namespace std;

int dx[] = { 0,0,1,-1 };
int dy[] = { 1,-1,0,0 };
int field[50][50] = { 1 };
int map[50][50] = { 0 };
queue<int, int> q;
int m, n, k;
int cur_x, cur_y, next_x, next_y;

bool check(int x, int y) {
	if (x < 0 || y < 0 || x >= n || y >= m) return false;
	return true;
}

void BFS(int a, int b) {
	q.push(pair < int, int >(a, b));
	field[a][b] = 0;
	while (!q.empty()) {
		cur_x = q.front().first;
		cur_y = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			next_x = cur_x + dx[i];
			next_y = cur_y + dy[i];

			if (check(next_y, next_x) && field[next_x][next_y]) {
				field[next_x][next_y] = 0;
				q.push(pair < int, int >(next_x, next_y));
				// q.push({next_x,next_y}); 형태로 중괄호를 써서 작성해주셔도 됩니다 저는 이걸 더 선호해요
			}
		}
	}
}

int main() {


	return 0;
}