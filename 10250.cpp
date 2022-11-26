#include <iostream>
using namespace std;

int main(void) {
	int t, h, w, n; //문제 내 입력받는 변수
	//실행횟수
	cin >> t;
	//t만큼 실행
	for (int k = 0; k < t; k++) {
		cin >> h >> w >> n;
		int count = 0;
		//각층의 x01호, x02호,,,,순으로 채워지므로 
		//for문을 h->w 순이아닌 w->h순으로 구성
		//count가 n이 될 때까지 방을 채워나감.
		for (int i = 1; i <= w; i++) {
			for (int j = 1; j <= h; j++) {
				count++;
				if (count == n) {
					if (i < 10) {
						cout << j << 0 << i << endl;
					}
					else {
						cout << j << i << endl;
					}

				}
				
			}
		}
	}
	return 0;
}