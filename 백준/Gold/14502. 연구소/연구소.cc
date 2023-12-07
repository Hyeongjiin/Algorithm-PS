#include <bits/stdc++.h>
using namespace std;
int N, M;
bool vis[8][8];
int space[8][8];
vector<pair<int, int>> v;
const int dy[] = {1, -1, 0, 0};
const int dx[] = {0, 0, 1, -1};

void dfs(int y, int x){
	if(space[y][x] == 1 || vis[y][x] == 1) return;
	vis[y][x] = 1;
	for(int i = 0; i < 4; i++){
		int ny = y + dy[i];
		int nx = x + dx[i];
		if(ny < 0 || nx < 0 || ny > N - 1 || nx > M - 1) continue;
		dfs(ny, nx);
	}
}

int solve(){
	memset(vis, 0, sizeof(vis));
	for(int i = 0; i < N; i++){
		for(int j = 0; j < M; j++){
			if(space[i][j] == 2){
				dfs(i, j);
			}
		}
	}
	int cnt = 0;
	for(int i = 0; i < N; i++){
		for(int j = 0; j < M; j++){
			if(space[i][j] == 0 && vis[i][j] == 0) cnt++;
		}
	}
	return cnt;
}

int main(){
	cin >> N >> M;
	for(int i = 0; i < N; i++){
		for(int j = 0; j < M; j++){
			cin >> space[i][j];
			if(space[i][j] == 0) v.push_back({i, j});
		}
	}
	int ans = 0;
	for(int i = 0; i < v.size() - 2; i++){
		for(int j = i + 1; j < v.size() - 1; j++){
			for(int k = j + 1; k < v.size(); k++){
				space[v[i].first][v[i].second] = space[v[j].first][v[j].second] = space[v[k].first][v[k].second] = 1;
				ans = max(ans, solve());
				space[v[i].first][v[i].second] = space[v[j].first][v[j].second] = space[v[k].first][v[k].second] = 0;
			}
		}
	}
	cout << ans;
	return 0;
}