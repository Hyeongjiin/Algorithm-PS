from collections import deque

def solution(begin, target, words):
    answer = 0
    print(answer)
    if target not in words:
        return answer
    else:
        visited = [False] * len(words)
        q = deque()
        q.append((begin, 0))
        while q:
            cur_word, cur_count = q.popleft()
            if cur_word == target:
                answer = cur_count
                return answer
            for idx, word in enumerate(words):
                if visited[idx] == False:
                    if diff(cur_word, word) == 1:
                        visited[idx] = True
                        q.append((word, cur_count + 1))
            
    return answer

def diff(A, B):
    count = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            count += 1
    return count