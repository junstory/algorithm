#include <iostream>
using namespace std;

int main(void){
	//입력 횟수 n과 각 시행마다 입력받을 수 k 
	int n,k;
	//소수의 개수 count 
	int count;
	cin >> n;
	//처음에 count를 n으로 정하고 소수가 아닐 때마다 1씩 빼는 방식.  
	count = n;
	for(int i =0; i<n;i++){
		cin >> k;
		//1은 소수가 아니므로 빼주고 continue 
		if(k==1){
			count--;
			continue;
		}
		//2는 소수이긴하나 %를 사용할 수가 없으므로 따로 지정함. 
		if(k==2){
			continue;
		}
		//그외의 수들은 2부터 자신-1의 수까지 %연산을 했을 때 0이 되면 count에서 1을 빼줌. 
		for(int j=2;j<k;j++){
			if(k%j==0){
				count--;
				//for문을 더 하면 -1이 아닌 -2,-3이 될 수도 있고
				//굳이 더 돌릴 이유도 없으므로 break
				break;  
			}
		}
	}
	//소수의 개수 출력  
	cout << count;
	return 0;
}
