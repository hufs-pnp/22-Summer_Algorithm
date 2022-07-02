#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<string> split(string s) {
    vector<string> v;
    
    int pos = s.find(" ");
    if (pos != -1) {
        string first = s.substr(0, pos);
        v.push_back(first);
        string second = s.substr(pos + 1, -1);
        v.push_back(second);
    }
    else {
        v.push_back(s);
    }

    return v;
}

int main()
{
    vector<int> v;
    int N;
    string s;
    vector<string> temp_s;

    cin >> N;
    cin.ignore();

    for (int i = 0; i < N; i++) {
        getline(cin, s);
        temp_s = split(s);
        if (temp_s[0] == "push") {
            v.push_back(stoi(temp_s[1]));
        }
        else if (temp_s[0] == "pop") {
            if (v.size() != 0) {
                cout << v.back() << endl;
                v.pop_back();
            }
            else {
                cout << -1 << endl;
            }
        }
        else if (temp_s[0] == "size") {
            cout << v.size() << endl;

        }
        else if (temp_s[0] == "empty") {
            if (v.size() == 0) {
                cout << 1 << endl;
            }
            else {
                cout << 0 << endl;
            }
        }
        else if (temp_s[0] == "top") {
            if (v.size() != 0) {
                cout << v.back() << endl;
            }
            else {
                cout << -1 << endl;
            }
        }
        
    }

    return 0;
}
