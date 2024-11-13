#include <iostream>
#include <string>
using namespace std;

int main() {
	string c;
	int count = 0;
	//공백을 입력받기 위해 줄을 입력받은 getline 사용
	getline(cin, c);
	
	//비어있다면 바로 0 출력 후 종료. 
	if(c.empty()){
		cout << 0 << endl;
		return 0;
	}
	//공백이 있다면 count 증가 
	for(int i = 0; i< c.length();i++){
		if(c[i]==' '){
			count++;
		}
	} 
	//index 0이 공백이면 단어가 없던 것이므로 감소 
	if(c[0]==' '){
		count--;
	}
	//마지막이 공백이 아니라면 마지막 단어를 세지 않았으므로 증가 
	if(c[c.length()-1]!=' '){
		count++;
	}
	
	cout << count << endl;
	
	return 0;
} 


