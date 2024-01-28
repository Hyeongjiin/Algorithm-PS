def solution(origin):
    print(origin)
    word = ['A', 'E', 'I', 'O', 'U']
    result = list(set(sequence(word)))
    result.sort()
    answer = 0
    for i in range(len(result)):
        if result[i] == origin:
            answer = i + 1
            break
    return answer


def sequence(data):
    def backtrack(curr, length):
        if len(curr) == length:
            result.append("".join(curr))
            return 
        for i in range(len(data)):
            curr.append(data[i])
            backtrack(curr, length)
            curr.pop()
    result = []
    for i in range(1, len(data) + 1):
        curr = []
        backtrack(curr, i)
    return result