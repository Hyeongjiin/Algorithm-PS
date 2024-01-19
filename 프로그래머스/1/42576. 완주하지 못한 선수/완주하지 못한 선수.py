def solution(participant, completion):
    members = {}
    answer = ''
    for i in completion:
        if i not in members:
            members[i] = 1
        else:
            members[i] += 1
    for i in participant:
        if i not in members:
            answer = i
            break
        else:
            members[i] -= 1
            if members[i] == -1:
                answer = i
                break
    return answer