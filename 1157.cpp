#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

int main() {
	//알파벳 개수를 담기위한 vector 
	vector<int> num(26);
	
	//입력을 위한 배열c /0를 생각해서 1을 더해줌 
    char c[1000001];
    cin >> c;
    //이유는 모르겠으나 strlen이 for문에서 바로 사용되지 않아서 사용했음. 
    int length = 0;
    length = strlen(c);
    for(int i=0; i<length; i++){
    	//소문자면 a를 대문자면 A를 빼서 index만 남도록 하는 과정. 
    	if(c[i] >90){
    		c[i]-='a';
		}
		else{
			c[i]-='A';
		} 
		num[c[i]]++;
	}
    
    //큰 값 찾기. 
	int MAX = 0;
	int idx = 0;
	for(int i=0; i<26;i++){
    	if(num[i]>MAX){
    		MAX = num[i];
    		idx = i;
		}
	}
	
	//큰 값을 찾는 과정에서 >을 썻기 때문에
	//그 다음 index부터 같거나 큰 값이 있으면 checked를 true로 바꾸어줌. 
	bool checked = false;
	for(int i=idx+1; i<26;i++){
    	if(num[i]>=num[idx]){
    		checked = true;
		}
	}
	//그에 따라 값 출력 
	if(checked){
		cout << "?" << endl;
	}
	else{
		char result = idx+'A';
		cout << result << endl;
	}
    
    //알파벳 개수 vector 출력하여 확인하는 코드. 
    //for(int i=0; i<26;i++){
    //	cout << num[i] << " ";
	//}
    
    return 0;
}
