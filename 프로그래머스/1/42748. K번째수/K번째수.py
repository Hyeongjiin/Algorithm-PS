def solution(array, commands):
    answer = []
    for command in commands:
        narr = sorted(array[command[0] - 1:command[1]])
        answer.append(narr[command[2] - 1])
    return answer