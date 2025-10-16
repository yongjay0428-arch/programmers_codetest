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
                    print(temp_answer)
                    for x in temp_answer[0]:
                        print(x)
                        if a < x[0] or b < x[1]-1:
                            break
                        else:
                            if park[x[0]][x[1]] != '-1':
                                break
                            else:
                                answer.append(len(x))




print(solution([5,3,2],
               [["A", "A", "-1", "B", "B", "B", "B", "-1"],
                ["A", "A", "-1", "B", "B", "B", "B", "-1"],
                ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"],
                ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"],
                ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"],
                ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]))