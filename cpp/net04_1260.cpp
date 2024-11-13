#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

vector<vector<int>> node;
vector<bool> is_visited;

void dfs(int cur) {
	is_visited[cur] = true;
	cout << cur<< " ";
	for (int i = 0; i < node[cur].size(); i++) {
		int next = node[cur][i];
		if (!is_visited[next]) {
			dfs(next);
		}
	}
}

void bfs(int start) {
	queue<int> q;
	q.push(start);
	is_visited[start] = true;

	while (!q.empty()) {
		int cur = q.front();
		q.pop();
		cout << cur << " ";
		for (int i = 0; i < node[cur].size(); i++) {
			int next = node[cur][i];
			if (!is_visited[next]) {
				q.push(next);
				is_visited[next] = true;
			}
		}
	}
}

int main() {
	int N, M,V;
	cin >> N >> M >> V;
	node.assign(N + 1, vector<int>(0, 0));
	is_visited.assign(N + 1, false);
	for (int i = 0; i < M; i++) {
		int a, b;
		cin >> a >> b;
		node[a].emplace_back(b);
		node[b].emplace_back(a);
	}

	
	for (int i = 1; i <= N;i++) {
		sort(node[i].begin(), node[i].end());

	}

	dfs(V);	
	is_visited.assign(N + 1, false);
	cout << '\n';
	bfs(V);

	return 0;
}