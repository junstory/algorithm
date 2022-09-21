#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main () {
	int a, b, ra, rb;
	ra = 0;
	rb = 0;
	//숫자를 역으로 바꾸기 위해 vector에 임시저장 
	vector<int> num;
	cin >> a >> b;
	while(a!=0){
		//한 자리씩 벡터에 넣고 자리수를 줄임 
		num.push_back(a%10);
		a /=10;
	}
	//cmath에 pow함수를 이용하여 뒤집은 숫자 ra만듦. 
	for(int i = 0;i<num.size();i++){
		ra+=num[i]*pow(10,num.size()-1-i);
	}
	
	//굳이 벡터를 하나더 선언하지 않기 위해 clear 
	num.clear();
	//같은 과정 반복 
	while(b!=0){
		num.push_back(b%10);
		b /=10;
	}
	for(int i = 0;i<num.size();i++){
		rb+=num[i]*pow(10,num.size()-1-i);
	}
	//추가적인 변수 선언 없이 삼항연산자 사용. 
	cout << (ra>rb ? ra : rb) << endl;
		
	return 0;
}
