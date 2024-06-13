def solution(friends, gifts):
    num = len(friends)
    # 친구들의 데이터를 저장할 사전
    info = dict()
    # 주고 받은 선물 데이터를 저장할 2차원 배열 
    data = [([0] * num) for _ in range(num)]
    # 선물 지수를 저장할 배열
    val = [0] * num
    # 최종적으로 받을 선물 개수 계산
    result = [0] * num

    # 각 이름마다 index 등록
    for i in range(len(friends)):
      info[friends[i]] = i

    # 서로 주고 받은 선물 기록
    for gift in gifts:
      relation = gift.split()
      data[info[relation[0]]][info[relation[1]]] += 1 

    # 선물 지수 계산
    for i in range(num):
      give = 0
      for j in range(num):
        give += data[i][j]
      take = 0
      for j in range(num):
        take += data[j][i]
      val[i] = give - take

    # 받을 선물 계산
    for i in range(num):
      for j in range(i + 1, num):
        if data[i][j] > data[j][i]:
          result[i] += 1
        elif data[i][j] < data[j][i]:
          result[j] += 1
        else:
          if val[i] > val[j]:
            result[i] += 1
          elif val[i] < val[j]:
            result[j] += 1

    answer = max(result)
    return answer