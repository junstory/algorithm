#include <iostream>
using namespace std;

//소수 판별 함수 
bool is_prime(int num){
	if(num==1){
		return false;
	}
	//for문을 num까지 반복하지 않고 제곱근num까지하면 더욱 효율적인 코드
	//제곱근까지만 해도 되는 이유는
	//2*4 = 4*2 인것 처럼 어느 시점부터는 위치만 바뀐 것이기 때문에
	//반으로 나눈 제곱근을 사용하는 것. 
	for(int j = 2;j<num;j++){
		if(num%j==0){
			return false;
		}
	}
	return true;
}

int main(void){
	int m,n;
	int sum=0;
	int min_prime;
	cin >> m;
	cin >> n;
	min_prime = n;
	//m과 n이 같은 수인 경우 1이면 -1
	//소수인 경우 그 수가 합과 동시에 최솟값. 
	if(m==n){
		if(m==1){
			cout << -1 << endl;
			return 0;
		}
		else if(is_prime(m)){
			cout << m << endl << m << endl;
			return 0;
		}
	}
	//같은 수가 아니면 for문으로 sum과 min을 구해줌 
	for(int i = m;i<=n;i++){
		if(i==2){
			sum+=i;
			min_prime=i;
			continue;
		}
		if(is_prime(i)){
			sum+=i;
			if(i<min_prime){
				min_prime = i;
			}
		}
	} 
	//합이 0이면 소수가 없었다는 뜻이므로 -1 출력 
	if(sum==0){
		cout << -1 << endl;
		return 0;
	}
	//그게 아니면 sum과 min_prime출력 
	cout << sum << endl << min_prime << endl;
	return 0;
} 
