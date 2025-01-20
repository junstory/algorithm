#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> v(n+1);
    vector<int> dp(n+1);
    
    for (int i = 1; i <= n; i++) {
        cin >> v[i];
    }
    
    if (n == 1) {
        cout << v[1] << endl;
        return 0;
    }
    if (n == 2) {
        cout << v[1] + v[2] << endl;
        return 0;
    }

    dp[1] = v[1];
    dp[2] = v[1] + v[2];
    dp[3] = max(v[1] + v[3], v[2] + v[3]);

    for (int i = 4; i <= n; i++) {
        dp[i] = max(dp[i - 2] + v[i], dp[i - 3] + v[i - 1] + v[i]);
    }

    cout << dp[n] << endl;
    return 0;
}

