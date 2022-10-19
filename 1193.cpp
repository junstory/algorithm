#include <iostream>
using namespace std;

int main(void){
	int n, diff; //입력받는 숫자 n , 줄에서 몇 번째에 위치하는지 구하기 위한 diff 
	int line = 0;//n이 위치한 줄 번호 
	int end = 0;//line까지의 모든 칸 개수 
	int top, bottom; //분자 , 분모 
	cin >> n;
	
	//대각선(/)으로 나누었을때 몇 번째 줄에 있는 지 확인 
	while(n>end){
		line += 1; 
		end +=line;  //1 + 2 + 3 + ... line을 더함으로써 모든 칸을 구함 / 다르 말로는 그 line의 마지막 index 
	}
	
	diff = end - n; // 그 line의 끝에서 얼마나 떨어져 있는가. 끝에서 떨어진 정도를 가지고 분수를 구함. 
	//line이 짝수면 시작에서 끝점으로 가면서
	//분모-- 분자++ / 홀수면 분모++ 분자--의 규칙을 가지고 있음
	if(line%2==0){
		top = line - diff; //분자는 line에서 diff만큼 뺀 값
		bottom = diff + 1; 
	} 
	else{
		top = diff + 1;
		bottom = line - diff;
	}
	cout << top << "/" << bottom << endl;
	return 0;
}
