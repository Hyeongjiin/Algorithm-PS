def solution(nums):
    pick = len(nums) / 2
    kind = len(set(nums))
    answer = min(pick, kind)
    return answer