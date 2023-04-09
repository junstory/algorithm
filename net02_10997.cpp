#include <iostream>
using namespace std;

char stars[100][100];
void draw_S(int N, int x, int y) {
	int width = 4 * (N - 1) + 1;
	int height = width - 2;
	//°¡·Î
	for(int i = x;i<width;i++){
		stars[y][i] = "*";
	}
}

int main() {
	int N;
	cin >> N;
	draw_S(N);
	return 0;
}