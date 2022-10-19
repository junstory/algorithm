#include <iostream>
using namespace std;

int main(void) {
	int a,b,v;
	cin >> a >> b >> v;
	
	//하루만에 올라가는 거리면 바로 1 출력 후 종료 
	if((v-a) <=0){
		cout << 1 << endl;
		return 0;
	}
	
	int day = 1; // v-a만큼만 가면 a만큼 가면 정상이므로 그걸 감안해서 day를 1로 해줌. 
	day += (v-a)/(a-b); //v-a만큼 하루에 a-b만큼 가므로 둘을 나눈 값을 day에 더함. 
	//더했는데도 나머지가 존재한다면
	//예를 들어 하루에 4씩 가는데 v-a까지 남은 거리가 2라도 어쩔 수 없이 4만큼 가야하므로
	//day++을 해줌. 
	if((v-a)%(a-b)>0){  
		day++;
	}
		
	cout << day;
	
	return 0;
} 
