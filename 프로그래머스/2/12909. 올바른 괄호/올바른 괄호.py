def solution(s):
    answer = True
    data = []
    for i in s:
        if i == '(':
            data.append(')')
        else:
            if data:
                data.pop()
            else:
                answer = False
                break
    if data:
        answer = False

    return answer