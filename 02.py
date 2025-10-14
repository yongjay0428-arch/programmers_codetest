def solution(mats, park):
    answer =0
    answer_list = []
    spaces=[]
    spaces_list=[]
    y=0
    for p in park:
        x = 0
        for space in p:
            if space == '-1':
                spaces.append([x,y])
            x +=1
        y+=1
    for loc in spaces:
        for m in mats:
            if [loc[0]+m,loc[1]+m] in spaces:
                spaces_list.append([loc,m])
    for loc2 in spaces_list:
        print(loc2)
        # print(loc2) #[2, 0], 5]
        for dist in range(1,loc2[1]):
            if [loc2[0][0]+dist,loc2[0][1]] in spaces and [loc2[0][0],loc2[0][1]+dist] in spaces and [loc2[0][0]+dist,loc2[0][1]+dist] in spaces:
                answer_list.append(loc2[1])
    answer = max(answer_list)
    return answer

print(solution([5,3,2],
               [["A", "A", "-1", "B", "B", "B", "B", "-1"],
                ["A", "A", "-1", "B", "B", "B", "B", "-1"],
                ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"],
                ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"],
                ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"],
                ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]))