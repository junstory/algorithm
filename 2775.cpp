#include <iostream>
using namespace std;

//재귀함수를 이용하여 해당 층의 사람 수를 구함.
//people_num의 매개변수는 a:층, b:호
//a층 b호 사람의 수는 (a-1층b호 + a층 b-1호)의 사람수와 같음 
int people_num(int a, int b){
	//0호는 존재하지 않으므로 0반환 
	if(b==0){
		return 0;
	}
	//0층에서는 호 만큼의 사람이 살고 있으므로 b반환 
	else if(a==0){
		return b;
	}
	//그게 아니면 재귀 함수를 이용하여 사람 수를 구함. 
	else return people_num(a,b-1)+people_num(a-1,b);
}

int main(void){
	int n, a, b;
	cin >> n;
	for(int i = 0; i< n ; i++){
		cin >> a;
		cin >> b;
		//출력 시 줄바꿈이 있어야 하므로 마지막에 endl 혹은 \n 필수. 
		cout << people_num(a,b) << endl;
	}
	return 0;
} 
