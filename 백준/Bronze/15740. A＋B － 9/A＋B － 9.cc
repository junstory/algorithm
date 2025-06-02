#include <iostream>
#include <string>
using namespace std;

// 앞자리 0 제거
string TrimLeadingZeros(const string& s) {
    size_t idx = 0;
    while (idx < s.size() - 1 && s[idx] == '0') idx++;
    return s.substr(idx);
}

// 절댓값 기준으로 a > b인지 판단
bool B_Abs(const string& a, const string& b) {
    string sa = TrimLeadingZeros(a);
    string sb = TrimLeadingZeros(b);
    if (sa.length() != sb.length()) return sa.length() > sb.length();
    return sa > sb;
}

// 문자열 덧셈: a + b (양수 전용)
string B_Add(const string& a, const string& b) {
    string result;
    int carry = 0;
    int i = (int)a.size() - 1, j = (int)b.size() - 1;

    while (i >= 0 || j >= 0 || carry) {
        int da = (i >= 0) ? a[i--] - '0' : 0;
        int db = (j >= 0) ? b[j--] - '0' : 0;
        int sum = da + db + carry;
        result.insert(result.begin(), (sum % 10) + '0');
        carry = sum / 10;
    }
    return result;
}

// 문자열 뺄셈: a - b (a >= b 가정)
string B_Subtract(const string& a, const string& b) {
    string result;
    int borrow = 0;
    int i = (int)a.size() - 1, j = (int)b.size() - 1;

    while (i >= 0) {
        int da = a[i--] - '0' - borrow;
        int db = (j >= 0) ? b[j--] - '0' : 0;
        if (da < db) {
            da += 10;
            borrow = 1;
        } else {
            borrow = 0;
        }
        result.insert(result.begin(), (da - db) + '0');
    }

    return TrimLeadingZeros(result);
}

// 덧셈 또는 뺄셈 연산 처리 (부호 포함)
string B_Oper(string a, string b) {
    bool ma = false, mb = false;
    if (a[0] == '-') {
        ma = true;
        a = a.substr(1);
    }
    if (b[0] == '-') {
        mb = true;
        b = b.substr(1);
    }

    string result;

    if (ma == mb) {
        result = B_Add(a, b);
        if (ma) result = '-' + result;
    } else {
        if (B_Abs(a, b)) {
            result = B_Subtract(a, b);
            if (ma) result = '-' + result;
        } else {
            result = B_Subtract(b, a);
            if (mb) result = '-' + result;
        }
    }

    result = TrimLeadingZeros(result);
    if (result == "0" || result == "-0") return "0";
    return result;
}

int main() {
    string ina, inb;
    cin >> ina >> inb;
    cout << B_Oper(ina, inb) << endl;
    return 0;
}