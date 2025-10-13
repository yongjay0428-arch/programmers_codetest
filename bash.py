# https://school.programmers.co.kr/learn/courses/30/lessons/340198
# def solution(mats, park):
#     answer = 0
#     for i in park:
#         for j in mats:
#             if [-1]*3 in j:
#                 pass
#     return answer

# def solution(mats, park):
#     plist=[]
#     answer = 0
#     y=0
#     for a in park:
#         x = 0
#         y +=1
#         for b in a:
#             x+=1
#             if b == "-1":
#                 plist.append([x,y])
#
#     for i in plist:
#         if

def solution(mats, park):
    plist=[]
    answer = 0
    y=0
    for a in park:
        x=0
        for b in a:
            if b != "-1":
                park[y][x]="1"
            x += 1
        y+=1

    for p in park:
        for m in mats[::-1]:
            line = "1"*m
            print(line.split(','))

print(solution([5,3,2],[["A", "A", "-1", "B", "B", "B", "B", "-1"], ["A", "A", "-1", "B", "B", "B", "B", "-1"], ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]]))