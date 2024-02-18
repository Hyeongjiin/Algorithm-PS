import sys

input = sys.stdin.readline
INF = int(1e20)
N, atk = map(int, input().split())
dungeon = []
for _ in range(N):
  dungeon.append(list(map(int, input().split())))

start_hp = 0
end_hp = INF
ans_hp = INF + 1

while start_hp <= end_hp:
  mid_hp = (start_hp + end_hp) // 2
  max_hp = mid_hp
  atk_c = atk
  for room in dungeon:
    if room[0] == 1:
      if room[2] % atk_c == 0:
        attackTime = room[2] // atk_c - 1
      else:
        attackTime = room[2] // atk_c
      max_hp -= attackTime * room[1]
      if max_hp <= 0:
        break
    elif room[0] == 2:
      atk_c += room[1]
      max_hp += room[2]
      if max_hp > mid_hp:
        max_hp = mid_hp

  if max_hp <= 0:
    start_hp = mid_hp + 1
  else:
    ans_hp = min(ans_hp, mid_hp)
    end_hp = mid_hp - 1
    
print(ans_hp)