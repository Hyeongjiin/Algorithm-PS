import sys

input = sys.stdin.readline

N = int(input())
data = []
end = 0
for i in range(N):
    time = input().split()
    if int(time[1]) > end:
        end = int(time[1])
    data.append((int(time[0]), int(time[1])))
data = sorted(data, key = lambda x:(x[1], x[0]))
current = data[0][0]
cnt = 0
for i in range(N):
    if current <= data[i][0]:
        cnt += 1
        current = data[i][1]
print(cnt)       