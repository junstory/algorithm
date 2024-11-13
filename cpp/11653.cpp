#include <iostream>
using namespace std;

int main (void){
	int n;
	int i = 2;
	cin >> n;
	//n이 1인 경우 아무 출력도 하지 않고 종료. 
	if(n == 1){
		return 0;
	}
	
	while(1){
		//n이 1이면 다 소인수분해가 완료된 것이므로 break 
		if(n==1){
			break;
		}
		//i는 2부터 시작하여 n을 i로 나눌 수 있다면 그 수를 출력하고 그 수로 나눔. 
		if(n%i==0){
			cout << i << endl;
			n=n/i;
		}
		//그렇지 않다면 i를 1씩 증가시키며 계속 반복 
		else{
			i++;
		}
	}
	
	return 0;
} 
