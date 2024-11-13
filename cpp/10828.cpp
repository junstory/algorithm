#include <iostream>
#include <string>
using namespace std;

//스택 : FILO(First In, Last Out)구조로, 택배 상하차에 비유를 하곤 합니다.
//먼저들어간 상자 보다 마지막에 넣은 상자가 제일 먼저 빠져나오는 모습과 동일하기 때문입니다.
class Stack {
	//private 변수로 데이터와 데이터의 크기를 알려주는 _size변수
private:
	int data[10001];
	int _size;
public:
	Stack() {
		_size = 0;
	}
	//1만 보다 크면 범위를 벗어나므로 그냥 return(함수종료)
	void push() {
		int temp;
		if (_size >= 10000) {
			return;
		}
		//그게 아니라면 _size 인덱스에 저장 후, 1증가
		cin >> temp;
		data[_size] = temp;
		_size++;
	}

	//비어있으면 -1 아니면 _size-1 출력. (개수는 인덱스와 하나 차이나므로). 
	void pop() {
		if (_size <= 0) {
			cout << -1 << '\n';
			return;
		}
		cout << data[_size-1] << '\n';
		_size--;
		if (_size < 0) {
			_size = 0;
		}
	}

	//_size변수 출력하면 끝.
	void size() {
		cout << _size << '\n';
	}

	void empty() {
		if (_size <= 0) {
			cout << 1 << '\n';
		}
		else {
			cout << 0 << '\n';
		}
	}

	//pop과 마찬가지로 스택이 비어있으면 -1 출력
	//아니라면 _size-1 출력.(맨 위칸 출력)
	void top() {
		if (_size <= 0) {
			cout << -1 << '\n';
		}
		else {
			cout << data[_size-1] << '\n';
		}
	}
};

int main(void) {
	int N;
	Stack stk;
	string cmd;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> cmd;
		if (cmd == "push") { stk.push(); }
		else if (cmd == "pop") { stk.pop(); }
		else if (cmd == "size") { stk.size(); }
		else if (cmd == "empty") { stk.empty(); }
		else if (cmd == "top") { stk.top(); }
	}

	return 0;
}