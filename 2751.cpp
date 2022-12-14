#include <iostream>
using namespace std;
int nums[1000001];
int num_temp[1000001];

void Merge(int nums[], int start, int mid, int end) {
	int i = start;
	int j = mid + 1;
	int t = start;
	while (i <= mid && j <= end) {
		if (nums[i] < nums[j]) {
			num_temp[t] = nums[i];
			i++;
		}
		else {
			num_temp[t] = nums[j];
			j++;
		}
		t++;
	}
	while (i <= mid) {
		num_temp[t] = nums[i];
		t++;
		i++;
	}
	while (j <= end) {
		num_temp[t] = nums[j];
		t++;
		j++;
	}
	t = start;
	while (t <= end) {
		nums[t] = num_temp[t];
		t++;
	}
}

void MergeSort(int nums[], int start, int end) {
	if (start < end) {
		int mid = (start + end) / 2;
		MergeSort(nums, start, mid);
		MergeSort(nums, mid + 1, end);
		Merge(nums, start, mid, end);
	}
}

int main(void) {
	int N, temp;
	cin >> N;
	
	//병합정렬(Merge Sort)
	//반씩 나누어 정렬시키고 다시 합치면서 정렬.
	for (int i = 0; i < N; i++) {
		cin >> temp;
		nums[i] = temp;
	}

	MergeSort(nums, 0, N-1);

	for (int i = 0; i < N; i++) {
		cout << nums[i] << '\n';
	}

	return 0;
}