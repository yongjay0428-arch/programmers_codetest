def square_cords(i, j, m):
    return [[r, c] for r in range(i, i + m) for c in range(j, j + m)]
def solution(mats,park):
    answer = []
    a = len(park)
    b = len(park[0])
    for i in range(a):
        for j in range(b):
            if park[i][j] != '-1':
                park[i][j] = '1'
    for m in mats:
        for i in range(a):
            for j in range(b):
                temp_answer=[]
                if park[i][j] =='-1':
                    temp_answer.append(square_cords(i,j,m))
                    temp_answer2=[]
                    for x in temp_answer[0]:
                        if a > int(x[0]) and b > int(x[1]) and park[x[0]][x[1]] == '-1':
                            temp_answer2.append([x[0],x[1]])
                        if temp_answer[0] == temp_answer2:
                            answer.append(len(temp_answer[0]))
    if len(answer) == 0:
        answer = -1
    else:
        answer = max(answer)**0.5
    return answer




print(solution([5,3,2],
               [["A", "A", "-1", "B", "B", "B", "B", "-1"],
                ["A", "A", "-1", "B", "B", "B", "B", "-1"],
                ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"],
                ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"],
                ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"],
                ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]))