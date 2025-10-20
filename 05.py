def solution(name, yearning, photo):
    answer = []
    for i in photo:
        temp_answer = 0
        for j in i:
            if j in name:
                idx=name.index(j)
                temp_answer+=yearning[idx]
        answer.append(temp_answer)
    return answer

print(solution(["may", "kein", "kain", "radi"],
               [5, 10, 1, 3],
               [["may", "kein", "kain", "radi"],
                    ["may", "kein", "brin", "deny"],
                    ["kon", "kain", "may", "coni"]]))