# https://school.programmers.co.kr/learn/courses/30/lessons/340199

def solution(wallet, bill):
    condition=True
    answer = 0
    while condition:
        bill = sorted(bill)
        wallet = sorted(wallet)
        if min(bill) > min(wallet) or max(bill) > max(wallet):
            answer +=1
            bill[1] = bill[1] // 2
        else:
            condition = False
    return answer

print(solution([50, 50],	[100, 241]))