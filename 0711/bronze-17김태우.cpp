// https://www.acmicpc.net/problem/2163
// 1x1 로 만들어야함
// 몇칸이던 간에 1xn or 1xm으로 나누어지고 이는 곧 n-1번 쪼개기 or m-1번 쪼개기가 된다
// 그리고 1xn, 1xm은 n-1, m-1 번 쪼개야한다.
// nxm -> n-1 쪼갬 -> n개의 1xm 블럭이 생김 -> n x (m-1) -> n-1 + n(m-1)
// nxm -> m-1 쪼갬 -> m개의 nx1 블럭이 생김 -> m x (n-1) - > m-1 + m(n-1)
// 
#include <iostream>

using namespace std;

// 쪼개는 수 구하기
int sp(int n, int m){
  int result = 0;

  result = (n - 1) + n * (m - 1);
  
  return result;
}

int main(){
  int N, M;

  cin >> N >> M;
  
  cout << sp(N,M);

  return 0;
}
