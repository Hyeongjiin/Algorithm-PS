def solution(bandage, health, attacks):
    att_num = len(attacks) 
    max_health = health
    for i in range(att_num - 1):
        health -= attacks[i][1]
        if health <= 0:
            break
        timeToHeal = attacks[i + 1][0] - attacks[i][0] - 1
        fullSkill = timeToHeal // bandage[0]
        health += timeToHeal * bandage[1] + fullSkill * bandage[2]
        if health > max_health:
            health = max_health
             
    health -= attacks[att_num - 1][1] 
    if health <= 0:
        health = -1
    answer = health
    return answer