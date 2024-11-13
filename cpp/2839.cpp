#include <iostream>
using namespace std;

//봉지의 개수를 담는 변수 count
//5로 나누어 진다면 5로 나눈값을 count에 더하고
//그렇지 않다면 무게(n)에서 3을 빼고 count에 1을 더한다.
//이 시행을 반복하다가 3보다 작다면 count를 -1로 정한뒤 출력 후,  종료시키고
//0이 된다면 count를 출력하며 종료한다. 
int main(void) {
	int n;
	int count = 0;
	cin >> n;
	while(1){
		//n이 3보다 작다면 더이상 나눌 수 없으므로 -1로 지정. 
		if(n<3){
			count = -1;
			break;
		}
		//5로 나누어 떨어진다면 몫을 더함.
		//더하는 이유는 3을 빼고 1을 더한 상태일 수도 있으므로 
		//=이 아닌 + 연산을 해주어야 함. 
		if(n%5==0){
			count += n/5;
			break;
		}
		else{
			n-=3;
			count++;
		}
		//n이 0일 때는 계산이 끝난 것이므로 while문을 탈출 시킴. 
		if(n==0){
			break;
		}
	} 
	//봉지의 개수 출력 
	cout << count << endl;

	return 0;
}
