// https://www.acmicpc.net/problem/1541
// +, - 만 사용
// 최소의 값을 낸다.
// -가 오면 그 뒤로는 그냥 다 빼면 됨
// 커밋 메세지 수정

#include <iostream>
#include <string.h>

using namespace std;

int main(){
  string s;
  bool pm = true;
  getline(cin, s);

  string temp="";
  int result = 0;

  for(int i=0; i<s.length(); i++){
    // not operator
    if(s[i]!='-' && s[i]!='+'){
      temp+=s[i];
      if (s[i + 1] == '+' || s[i + 1] == '-' || s[i+1] == '\0')
      {
        // true => 더하기
        if (pm)
        {
          result += stoi(temp);
          temp = "";
        }
        else
        {
          result -= stoi(temp);
          temp="";
        }
      }
    }else{
      if(s[i]=='-'){
        pm = false;
      }
    }
  }
  cout << result << endl;
  return 0;
}
