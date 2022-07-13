// https://www.acmicpc.net/problem/2644

#include <iostream>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;

int ct = -1;
int final = -1;
int people[100][100];
int visit[100];

void checkc(int n, int start, int goal){
  ct++;
  visit[start] = 1;

  if(start == goal){
    final = ct;
    return;
  }

  for(int i = 1; i<=n; i++){
    if(visit[i]==1)
      continue;
    if(people[start][i]!=1)
      continue;
    checkc(n,i,goal);
  }
  ct--;
  return;
}

int main(){
  int n,m,x,y; // 사람 수, 관계 수, 사람 번호
  int a, b; // 찾을 관계 사람 번호

  cin >> n; // 사람 수
  cin >> a >> b; // 관계를 찾을 사람의 번호
  cin >> m;
  // 각 사람들의 관계 입력
  while(m>0){
    m--;
    cin >> x >> y;
    people[x][y] = 1;
    people[y][x] = 1;
  }

  checkc(n,a,b);

  cout << final;

  return 0;
}
