#include <iostream>
#include <string>
#include <vector>
using namespace std;
//참고 : https://cryptosalamander.tistory.com/15 
int main() {
	//크로아티아 알파벳을 vector에 저장 
	vector<string> croat = {"c=","c-","dz=","d-","lj","nj","s=","z="};
	int idx;
	string str;
	cin >> str;
	
	//각각의 알파벳을 문자열에서 찾고
	//그 값을 임의의 # 으로 바꿔주는 과정 
	//단어의 개수가 중요하기 때문에 
	//ex) c=을 그냥 # 하나로 바꾸어 세기 쉽게 함. 
	for(int i = 0; i<croat.size();i++){
		while(1){
			idx = str.find(croat[i]);
			if(idx == str.npos){
				break;
			}
			str.replace(idx,croat[i].length(),"#");
		}
	}
	//그렇게 바뀐 문자열의 길이 출력 
	cout << str.length() << endl;
	
	return 0;
}
