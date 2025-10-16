def solution(record):
    members ={}
    changes = {}
    leaves = []
    list1 =[ ]
    answer = []

    for x in record:
        list1.append(x.split(' '))
    for a in list1:
        if a[0] == 'Enter':
            members[a[1]] =  a[2]
        if a[0] == 'Change':
            members[a[1]] = a[2]
        if a[0] == 'Leave':
            leaves.append(a[1])

    for x in list1:
        if x[0] == 'Enter':
            answer.append(f'{members[x[1]]}님이 들어왔습니다.')
        elif x[0] == 'Leave': answer.append(f'{members[x[1]]}님이 나갔습니다.')
    return answer

print(solution(["Enter uid1234 Muzi",
                "Enter uid4567 Prodo",
                "Leave uid1234",
                "Enter uid1234 Prodo",
                "Change uid4567 Ryan"]))