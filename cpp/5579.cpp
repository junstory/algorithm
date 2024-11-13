#include <iostream>
using namespace std;

int main(void) {
	int stu_num;
	//낸 학생들을 확인하기 위한 bool형 배열. 1번의 index를 1로 하기 위해 31까지 선언.
	//또한 다른 값이 들어가지 않도록 0으로 초기화.
	bool checked[31] = { 0 };
	
	//입력을 받아가며 낸 학생의 인덱스를 1로 바꿈.
	for (int i = 1; i <= 28; i++) {
		cin >> stu_num;
		checked[stu_num] = 1;
	}

	//두 명을 출력한 경우 멈추기 위한 num 변수 정의 및 제출하지 않은 학생 확인.
	int num = 0;
	for (int i = 1; i <= 30; i++) {
		
		if (checked[i] == 0) {
			cout << i << endl;
			num++;
		}
		if (num == 2) {
			break;
		}
	}

	return 0;
}