from sys import stdin
def solve():
    n=int(stdin.readline().rstrip())
    dic={}
    trash=0
    ltrash={}
    for i in range(n):
        a,b=map(int,stdin.readline().split())
        if a not in dic and b!=a: dic[a]=b
        elif b==a:
            trash+=1
            if b not in ltrash: ltrash[b]=0
        elif dic[a]>b and b!=a: dic[a]=b 
    for e in ltrash:
        if e not in dic:
            dic[e]=e
            trash-=1
    arr=list(dic)
    arr.sort()
    tmp=dic[arr[0]]
    cnt=1
    for i in range(1,len(arr)):
        if tmp>dic[arr[i]]:
            tmp=dic[arr[i]]
        else:
            if arr[i]>=tmp:
                cnt+=1
                tmp=dic[arr[i]]
    print(cnt+trash)
solve()