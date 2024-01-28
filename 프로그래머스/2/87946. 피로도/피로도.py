def solution(k, dungeons):
    answer = -1
    results = sequence(dungeons, len(dungeons))
    max_count = 0
    for result in results:
        piro = k
        count = 0
        for i in result:
            if piro >= i[0]:
                piro -= i[1]
                count += 1
        max_count = max(max_count, count)
    answer = max_count
    return answer

def sequence(data, length):
    def backtrack(curr):
        if len(curr) == length:
            result.append(curr[:])
            return result
        
        for i in range(len(data)):
            if visited[i] == False:
                curr.append(data[i])
                visited[i] = True
                backtrack(curr)
                curr.pop()
                visited[i] = False
    result = []
    curr = []
    visited = [False] * length
    backtrack(curr)
    return result