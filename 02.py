import numpy as np
def solution(mats,park):
    answer = []
    a = len(park)
    b = len(park[0])

    def square_coords(i, j, m):
        return [(r, c) for r in range(i, i + m) for c in range(j, j + m)]

    for i in range(a):
        for j in range(b):
            if park[i][j] != '-1':
                park[i][j] = '1'
    for j in range(b):
        temp_answer=[]
        if park[i][j] ==['1']:
            pass

print(solution([5,3,2],
               [["A", "A", "-1", "B", "B", "B", "B", "-1"],
                ["A", "A", "-1", "B", "B", "B", "B", "-1"],
                ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"],
                ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"],
                ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"],
                ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]))