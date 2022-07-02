// Example program
#include <iostream>
#include <string>

using namespace std;

int main()
{
    string s;
    int count = 0;
    
    getline(cin,s);
    
    
    for(int i=0; i<s.length(); i++){
        if(s[i] != ' ' && (s[i+1] == ' ' || s[i+1] == '\0')){
            count++;
        }
    }
    cout << count;
    return 0;
}
