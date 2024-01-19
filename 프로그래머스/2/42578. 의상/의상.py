def solution(clothes):
    kind = {}
    answer = 1
    for clothe in clothes:
        if clothe[1] not in kind:
            kind[clothe[1]] = 1
        else:
            kind[clothe[1]] += 1
    
    for value in kind.values():
        answer *= value + 1
    
    answer -= 1
            
    return answer