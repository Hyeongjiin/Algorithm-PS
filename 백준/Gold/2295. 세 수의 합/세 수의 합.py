import sys

sys = sys.stdin.readline

N = int(input())
data = set()
nums = []
for _ in range(N):
  nums.append(int(input()))

for i in range(N):
  for j in range(N):
    data.add(nums[i] + nums[j])

answer = 0

for i in range(N):
  for j in range(N):
    diff = nums[i] - nums[j]
    if diff in data:
      answer = max(answer, nums[i])

print(answer)