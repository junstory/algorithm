#include <iostream>
#include <cstring>
using namespace std;

int main() {
	char c[16];
	char p;
	int time = 0;
	cin >> c;
	for(int i=0;i<strlen(c);i++){
		p = c[i];
		//아스키코드를 이용하여 time에 더함. 
		if(p>64&&p<68){
			time +=3;
		}
		else if(p>67&&p<71){
			time +=4;
		}
		else if(p>70&&p<74){
			time +=5;
		}
		else if(p>73&&p<77){
			time +=6;
		}
		else if(p>76&&p<80){
			time +=7;
		}
		else if(p>79&&p<84){
			time +=8;
		}
		else if(p>83&&p<87){
			time +=9;
		}
		else if(p>86&&p<91){
			time +=10;
		}
		else{
			time+=11;
		}
	}
	
	//결과 출력 
	cout << time << endl;
	
	return 0;
} 
