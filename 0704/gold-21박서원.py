class dice:
    def __init__(self, n,m,y,x,k, map_):
        self.mapsize = [n,m]; self.loc = [y,x]; self.cmd_ = k
        self.mapnum = map_;
        self.dx = [0,1,-1, 0, 0]; self.dy = [0,0,0,-1,1]; self.tmp = [0]*7
    def check(self, i):
        y,x = self.loc[0], self.loc[1];
        if 0<=self.dx[i]+x and self.dx[i]+x<self.mapsize[1] and 0<=self.dy[i]+y and self.dy[i]+y<self.mapsize[0]:
            self.loc[0] += self.dy[i]; self.loc[1] += self.dx[i]; 
            return 1
        return 0
    def east(self): 
        self.tmp[1], self.tmp[4] = self.tmp[4],self.tmp[1]; 
        self.tmp[4], self.tmp[6] = self.tmp[6],self.tmp[4]; 
        self.tmp[3], self.tmp[6] = self.tmp[6],self.tmp[3];
    def west(self):
        self.tmp[1], self.tmp[3] = self.tmp[3],self.tmp[1]; 
        self.tmp[3], self.tmp[6] = self.tmp[6],self.tmp[3]; 
        self.tmp[4], self.tmp[6] = self.tmp[6],self.tmp[4];
    def north(self):
        self.tmp[1], self.tmp[5] = self.tmp[5],self.tmp[1]; 
        self.tmp[5], self.tmp[6] = self.tmp[6],self.tmp[5]; 
        self.tmp[2], self.tmp[6] = self.tmp[6],self.tmp[2];
    def south(self):
        self.tmp[1], self.tmp[2] = self.tmp[2],self.tmp[1]; 
        self.tmp[2], self.tmp[6] = self.tmp[6],self.tmp[2]; 
        self.tmp[5], self.tmp[6] = self.tmp[6],self.tmp[5];
    def ans(self):
        y,x = self.loc[0], self.loc[1]
        if self.mapnum[y][x] != 0: self.tmp[6] = self.mapnum[y][x];self.mapnum[y][x] = 0
        else: self.mapnum[y][x] = self.tmp[6]
        print(self.tmp[1])


n,m,y,x,k = map(int, input().split())
map_ = [list(map(int, input().split())) for _ in range(n)]
cmd = list(map(int, input().split()))

game = dice(n,m,y,x,k, map_)
for i in cmd:
    if game.check(i):
        if i == 1: game.east()
        elif i == 2: game.west()
        elif i == 3: game.north()
        elif i==4: game.south()
        game.ans()
