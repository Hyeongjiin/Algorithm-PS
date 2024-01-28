def solution(numbers):
    papers = list(numbers)
    result = list(set(sequence(papers)))
    answer = 0
    print(result)
    for i in result:
        if prime(i):
            answer += 1

    return answer

def sequence(data):
    def backtrack(curr, length):
        if len(curr) == length:
            result.append(int(''.join(curr)))
            return 
        for i in range(len(data)):
            if visited[i] == False:
                curr.append(data[i])
                visited[i] = True
                backtrack(curr, length)
                curr.pop()
                visited[i] = False
    result = []
    for i in range(1, len(data) + 1):
        curr = []
        visited = [False] * len(data)
        backtrack(curr, i)
    return result

def prime(num):
    answer = True
    if num < 2:
        return False
    if num == 2:
        return answer
    for i in range(2, num):
        if num % i == 0:
            answer = False
            break
    return answer