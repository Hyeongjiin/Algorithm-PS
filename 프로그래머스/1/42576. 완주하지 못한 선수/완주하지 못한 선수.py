def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    while completion:
        par = participant.pop()
        com = completion.pop()
        if par != com:
            answer = par
            break
    if answer == '':
        answer = participant.pop()
    return answer