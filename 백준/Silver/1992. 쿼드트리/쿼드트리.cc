#include <bits/stdc++.h>
using namespace std; 
int N;
int space[64][64];

void quad(int sy, int sx, int scale){
	int base = space[sy][sx];
	int flag = 0;
	for(int i = 0; i < scale; i++){
		if(flag) break;
		for(int j = 0; j < scale; j++){
			if(space[sy + i][sx + j] != base){
				flag = 1;
				break;
			}
		}
	}
	if(flag){
		printf("(");
		quad(sy, sx, scale / 2);
		quad(sy, sx + scale / 2, scale / 2);
		quad(sy + scale / 2, sx, scale / 2);
		quad(sy + scale / 2, sx + scale / 2, scale / 2);
		printf(")");
	}
	else{
		printf("%d", base);
	}
}

int main(){
	scanf("%d", &N);
	for(int i = 0; i < N; i++){
		for(int j = 0; j < N; j++){
			scanf("%1d", &space[i][j]);	
		}
	}
	quad(0, 0, N);
    return 0;
} 