#include <bits/stdc++.h>
using namespace std; 
int N, M;
int space[100][100];
int visited[100][100];
const int dy[] = {1, -1, 0, 0};
const int dx[] = {0, 0, 1, -1};

void bfs(int y, int x){
	queue<pair<int, int>> q;
	q.push({y, x});
	visited[y][x] = 1;
	while(q.size()){
		tie(y, x) = q.front();
		if(y == N - 1 && x == M - 1) break;
		q.pop();
		for(int i = 0; i < 4; i++){
			int ny = y + dy[i];
			int nx = x + dx[i];
			if(ny < 0 || nx < 0 || ny > N - 1 || nx > M - 1) continue;
			if(!visited[ny][nx] && space[ny][nx] == 1){
				space[ny][nx] = space[y][x] + 1;
				q.push({ny, nx});
			}
		}
		
	}
}

int main(){
	scanf("%d %d", &N, &M);
	for(int i = 0; i < N; i++){
		for(int j = 0; j < M; j++){
			scanf("%1d", &space[i][j]);
		}
	}
	bfs(0, 0);
	cout << space[N - 1][M - 1];
    return 0;
} 