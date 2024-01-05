#include <bits/stdc++.h>
using namespace std;
int N, M;
int space[100][100];
bool air[100][100];
const int dy[] = {1, -1, 0, 0};
const int dx[] = {0, 0, 1, -1}; 

void bfs(int y, int x){
	memset(air, 0, sizeof(air));
	queue<pair<int, int>> q;
	q.push({y, x});
	air[y][x] = 1;
	while(q.size()){
		tie(y, x) = q.front();
		q.pop();
		for(int i = 0; i < 4; i++){
			int ny = y + dy[i];
			int nx = x + dx[i];
			if(ny < 0 || nx < 0 || ny > N - 1 || nx > M - 1) continue;
			if(space[ny][nx] == 0 && air[ny][nx] == 0){
				q.push({ny, nx});
				air[ny][nx] = 1;
			}
		}
	}
}

int check(int y, int x){
	for(int i = 0; i < 4; i++){
		int ny = y + dy[i];
		int nx = x + dx[i];
		if(ny < 0 || nx < 0 || ny > N - 1 || nx > M - 1) continue;
		if(space[ny][nx] == 0 && air[ny][nx] == 1){
			space[y][x] = 0;
			return 1;	
		}
	}
	return 0;
}

int main(){
	cin >> N >> M;
	for(int i = 0; i < N; i++){
		for(int j = 0; j < M; j++){
			cin >> space[i][j];
		}
	}
	int clo = 0;
	int rem = 0;
	while(true){
		int cnt = 0;
		bfs(0, 0);
		for(int i = 0; i < N; i++){
			for(int j = 0; j < M; j++){
				if(space[i][j] == 1){
					cnt += check(i, j);
				}
			}
		}
		clo++;
		if(cnt == 0) break;
		rem = cnt;	
	}
	cout << clo - 1 << "\n" << rem;
	return 0;
}