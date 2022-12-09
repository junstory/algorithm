#include <iostream>
using namespace std;

int nums[10001] = { 0 };
int main(void) {
	//수의 범위가 10000이므로 카운팅 정렬 사용 예정.

	//동기화를 비활성화 시키고, cin과 cout 묶음을 해제해 줌으로써 실행속도를 높임.
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	int N, temp;;
	cin >> N;
	//카운팅 정렬
	//같은 수를 여러 번(j) 정렬해야 한다는 것은
	//그 수를 j번 출력해주는 것과 같다.
	//index와 수가 같도록 nums를 10001배열로 만들고
	//해당 수를 입력받으면 해당 index값을 1 증가.
	for (int i = 0; i < N; i++) {
		cin >> temp;
		nums[temp]++;
	}
	
	//0이 아닌 경우 해당 수를 nums에 있는 횟수만큼 출력.
	for (int i = 1; i < 10001; i++) {
		if (nums[i] != 0) {
			for (int j = 0; j < nums[i]; j++) {
				cout << i << '\n';
			}
		}
	}

	return 0;
}