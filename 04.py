def solution(s):
    answer = 0
    slist=s.split(' ')
    for i in range (len(slist)):
        if slist[i] != "Z":
            answer += int(slist[i])
        else:
            answer -= int(slist[i-1])
    return answer

print(solution("1 2 Z 3"))
print(solution("10 20 30 40"))
print(solution("10 Z 20 Z 1"))
print(solution("10 Z 20 Z"))