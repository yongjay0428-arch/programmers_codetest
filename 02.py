# https://school.programmers.co.kr/learn/courses/30/lessons/340198

def solution(mats, park):
    answer = []
    answer1=[]
    answer2=[]
    y=0
    for p in park:
        for i in range(0,len(park)):
            if p[i] == "-1":
                for m in mats:
                    if set(p[i:i+m]) == {'-1'}:
                        answer.append([y,i,i+m])
        y+=1
    for a in range(0,len(answer)):
        for m in mats:
            for idx in range(0, m):
                answer1=answer.copy()
                answer1[a][0]=answer1[a][0]+idx
                answer2.append(answer1[a])
    return answer2

print(solution([5,3,2],
               [["A", "A", "-1", "B", "B", "B", "B", "-1"],
                ["A", "A", "-1", "B", "B", "B", "B", "-1"],
                ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"],
                ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"],
                ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"],
                ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]))