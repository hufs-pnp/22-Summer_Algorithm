// boj 1009
// 나머지에 해당하는 번호에서 작업 수행
// 다만 제곱 연산을 하기에는 낭비인 것 같음

#include <iostream>

using namespace std;

int square(int a, int b){
  int t = 1;
  while(b>0){
    t *= a;
    if(t > 10){
      t %= 10;
    }
    
    b--;
  }
  
  return t;
}

int main(){
  int T;
  int a, b;

  cin >> T;

  while(T>0){
    cin >> a >> b;
    int result = square(a, b);
    int num = result % 10;
    if(num==0){
      cout << 10 << endl;
    }
    else{
      cout << num << endl;
    }

    T--;
  }

  return 0; 
}
