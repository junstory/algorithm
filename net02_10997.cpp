#include <iostream>
using namespace std;

char stars[400][400];
void draw_S(int N, int x, int y) {
	int width = 4 * N - 3;
	int height = width + 2;
	// <-
	for(int i = 1;i<width;i++){
		stars[x][y--] = '*';
	}
	//¾Æ·¡
	for (int i = 1; i < height; i++) {
		stars[x++][y] = '*';
	}
	// ->
	for (int i = 1; i < width; i++) {
		stars[x][y++] = '*';
	}
	//À§
	for (int i = 1; i < height-2; i++) {
		stars[x--][y] = '*';
	}
	stars[x][y] = '*';
	y--;
	stars[x][y] = '*';

	if (N == 2) {
		stars[x][y - 1] = '*';
		stars[x + 1][y - 1] = '*';
		stars[x + 2][y - 1] = '*';
		return;
	}

	draw_S(N - 1, x, y - 1);
}

int main() {
	int N;
	cin >> N;
	if (N == 1) {
		cout << '*';
		return 0;
	}
	int width = 4 * N - 3;
	int height = width + 2;

	for (int i = 0; i < height; i++) {
		for (int j = 0; j < width; j++) {
			stars[i][j] = ' ';
		}
	}
	int x = 0;
	int y = 4 * N - 4;

	draw_S(N,x,y);

	for (int i = 0; i < height; i++) {
		if (i == 1){
			cout << "*\n";
			continue;
		}
		for (int j = 0; j < width; j++) {
			cout << stars[i][j];
		}
		cout << '\n';
	}
	return 0;
}