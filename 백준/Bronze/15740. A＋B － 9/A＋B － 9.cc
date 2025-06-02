#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

bool B_Abs(string a, string b) {
    if (a.length() != b.length()) return a.length() > b.length();
    for (size_t i = 0; i < a.length(); ++i) {
        if (a[i] != b[i]) return a[i] > b[i];
    }
    return false;
}
string B_Add(string a, string b) {
    if (a.length() < b.length()) swap(a, b);
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    string result = "";
    int up = 0;
    for (size_t i = 0; i < a.length(); i++) {
        int A_a = a[i] - '0';
        int A_b = (i < b.length() ? b[i] - '0' : 0);
        int sum = A_a + A_b + up;
        result += (sum % 10) + '0';
        up = sum / 10;
    }
    if (up) {
        result += up + '0';
    }
    reverse(result.begin(), result.end());
    return result;
}

string B_Subtract(string a, string b) {
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    string result = "";
    int down = 0;
    for (size_t i = 0; i < a.length(); i++) {
        int S_a = a[i] - '0' - down;
        int S_b = (i < b.length() ? b[i] - '0' : 0);
        if (S_a < S_b) {
            S_a += 10;
            down = 1;
        } else {
            down = 0;
        }
        result += (S_a - S_b) + '0';
    }
    while (result.length() > 1 && result.back() == '0') {
        result.pop_back();
    }
    reverse(result.begin(), result.end());
    return result;
}

string B_Oper(string a, string b) {
    bool ma = false;
    bool mb = false;
    if (a[0] == '-') {
        a = a.substr(1);
        ma = true;
    }
    if (b[0] == '-') {
        b = b.substr(1);
        mb = true;
    }
    if (ma == mb) {
        string result = B_Add(a, b);
        if (ma) {
            result = '-' + result;
        }
        return result;
    } 
    if (B_Abs(a, b)) {
        string result = B_Subtract(a, b);
        if (ma) {
            result = '-' + result;
        }
        return result;
    } else {
        string result = B_Subtract(b, a);
        if (mb) {
            result = '-' + result;
        }
        return result;
    }
    
}


int main() {
    string ina, inb;
    cin >> ina >> inb;
    string result = B_Oper(ina, inb);
    cout << result;
}