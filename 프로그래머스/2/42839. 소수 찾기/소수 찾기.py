def solution(numbers):
    '''   
    전부 다 일일이 소수 계산
    papers = list(numbers)
    result = list(set(sequence(papers)))
    answer = 0
    print(result)
    for i in result:
        if prime(i):
            answer += 1 
    '''
    # 에라토스테네스의 체 사용해 소수 판별하기
    papers = list(numbers)
    result = list(set(sequence(papers)))
    result.sort()
    answer = 0
    max_num = max(result)
    table = [True] * (max_num + 1)
    for i in range(2, max_num + 1):
        if table[i] == True:
            j = 2
            while i * j <= max_num:
                table[i * j] = False
                j += 1                
    for i in result:
        if i < 2:
            continue
        if table[i] == True:
            answer += 1

    return answer

# 숫자 조합 만들기 - visited를 통해 사용한 숫자 재사용 하지 않기
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

# 일일이 소수 판별하기 
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