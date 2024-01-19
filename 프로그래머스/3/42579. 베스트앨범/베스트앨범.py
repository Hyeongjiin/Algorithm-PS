def solution(genres, plays):
    total = {}
    data = []
    for i in range(len(plays)):
        if genres[i] not in total:
            total[genres[i]] = plays[i]
        else:
            total[genres[i]] += plays[i]
        data.append((genres[i], plays[i], i))
    result = []
    for i, j in total.items():
        result.append((i, j))
    result.sort(key = lambda x : -x[1])
    data.sort(key = lambda x : (x[0], -x[1]))
    answer = []
    for i in range(len(result)):
        count = 2
        for j in range(len(data)):
            if result[i][0] == data[j][0]:
                answer.append(data[j][2])
                count -= 1
                if count == 0:
                    break
            
    return answer