#include <iostream>
using namespace std;
int a[500001];
int sorted[500001];
int mode[8001];
void merge(int a[], int start,int mid, int end) {
	int init_start = start;
	int idx = start;
	int mid_start = mid + 1;
	while (init_start <= mid && mid_start <= end) {
		if (a[init_start] <= a[mid_start]) {
			sorted[idx] = a[init_start];
			init_start++;
		}
		else {
			sorted[idx] = a[mid_start];
			mid_start++;
		}
		idx++;
	}
	if (init_start > mid) {
		while (mid_start <= end) {
			sorted[idx] = a[mid_start];
			mid_start++;
			idx++;
		}
	}
	else {
		while (init_start <= mid) {
			sorted[idx] = a[init_start];
			init_start++;
			idx++;
		}
	}
	
	for (int i = start; i <= end; i++) {
		a[i] = sorted[i];
	}
}

void merge_sort(int a[],int start, int end) {
	int mid;
	if (start >= end) {
		return;
	}
	mid = (start + end) / 2;
	merge_sort(a,start,mid);
	merge_sort(a, mid + 1, end);
	merge(a, start,mid, end);
}
int main() {
	int n,temp;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> temp;
		a[i] = temp;
	}
	merge_sort(a, 0, n-1);
	

	int sum = 0;
	for (int i = 0; i < n; i++) {
		sum += a[i];
		mode[a[i] + 4000]++;
	}
	cout << "\n";
	cout << sum / n << '\n';

	cout << a[n / 2] << '\n';

	int idx = 0;
	int count = 0;
	for (int i = 0; i < n; i++) {
		if (mode[i] > count) {
			count = a[i];
			idx = i;
		}
	}
	for (int i = idx+1; i < n; i++) {
		if (mode[i] == count) {
			idx = i;
			break;
		}
	}
	cout << a[idx] << '\n';
	
	cout<< a[n-1] - a[0] << '\n';
	return 0;
}