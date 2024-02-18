import sys

input = sys.stdin.readline
N, atk = map(int, input().split())
hp = 0
dungeon = []
atk_c = atk
for _ in range(N):
  kind, dataF, dataS = map(int, input().split())
  dungeon.append([kind, dataF, dataS])
  if kind == 1:
    if dataS % atk_c == 0:
      attackTime = dataS // atk_c - 1
    else:
      attackTime = dataS // atk_c
    hp += attackTime * dataF
  elif kind == 2:
    atk_c += dataF

start_hp = 0
end_hp = hp * 2
ans_hp = hp * 2 + 1

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
