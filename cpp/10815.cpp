#include <iostream>
#include <algorithm>
using namespace std;

//algorithm 헤더 파일을 이용하여 정렬 후, 이진탐색 활용
//원하는 num이 nums의 중앙값이라면 1 반환
//아니라면,
//nums의 값이 더 크다면 값을 낮추도록 end를 mid-1로 설정
//아니라면 start를 mid+1로 설정하면서 점차 원하는 num에 도달
int nums[500001];
int Binary_S(int num, int N) {
	int start = 0;
	int end = N - 1;
	int mid;
	while (start <= end) {
		mid = (start + end) / 2;
		if (nums[mid] == num) {
			return 1;
		}
		else if (nums[mid] > num) {
			end = mid - 1;
		}
		else {
			start = mid + 1;
		}
	}
	return 0;
}

int main(void) {
	int N, M, temp;

	//시간초과문제를 없애기 위해 사용
	ios_base::sync_with_stdio(0); cin.tie(0);

	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> temp;
		nums[i] = temp;
	}

	sort(nums, nums + N);

	cin >> M;
	for (int i = 0; i < M; i++) {
		cin >> temp;
		cout << Binary_S(temp, N) << ' ';
	}
	cout << '\n';

	return 0;
}