def solution(routes):
    routes.sort(key = lambda x : (x[0], x[1]))
    print(routes)
    start = routes[0][0]
    end = routes[0][1]
    answer = 1
    for route in routes:
        if start <= route[0] <= end:
            start = max(start, route[0])
            end = min(end, route[1])
        else:
            start = route[0]
            end = route[1]
            answer += 1
    return answer