#include <iostream>
#include <string>
using namespace std;
//참고: https://jaynamm.tistory.com/entry 
int main() {
	string word;
	int n;
	cin >> n;
	int count = 0;
	
	for(int i= 0; i< n; i++){
		cin >> word;
		bool yes = true;
		for(int j = 0; j< word.length();j++){
			for(int k =0; k< j;k++){
				//word[j]!=word[j-1]&&word[j]==word[k]
				//이전 index값이 다른 와중에  
				//0부터 index전까지 
				//자신과 같은게 있다면 그룹단어가 아님. 
				if(word[j]!=word[j-1]&&word[j]==word[k]){
					yes = false;
				}
			}
		}
		if(yes){
			count++;
		}
	}
	cout << count << endl;
	return 0;
}
