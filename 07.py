def split_numbers(i,j):
    numbers=list(range(1,i+1)) # 모든 상자가 포함된 리스트 numbers 생성
    return [numbers[i:i+j] for i in range(0,len(numbers),j)] #j의 길이를 가지는 리스트 생성, w만큼 끊어서 생성

def solution(n, w, num):
    answer = 0
    piles=[]
    pile=split_numbers(n,w) #pile에 끊어준 list 담아주기
    aloc=[]

    for i in pile: # 좌측 기준으로 인덱스 재배열
        temp=[]
        for j in i:
            if pile.index(i)%2==0:
                temp.append(j)
            else:
                temp.append(j)
                temp.sort(reverse=True)
        piles.append(temp)
    # print(piles) [[1, 2, 3, 4, 5, 6], [12, 11, 10, 9, 8, 7], [13, 14, 15, 16, 17, 18], [22, 21, 20, 19]]
    for i in piles:
        if num in i:
            aloc=[piles.index(i),i.index(num)]
    # print(aloc) [1,4] 꺼내야하는 목표 상자가 위치한 좌표 찾기

    for i in piles:
        if piles.index(i) % 2 == 0:
            if len(i) >= aloc[1]+1:
                answer += 1
        else:
            if len(i) + aloc[1] >= w-2:
                answer += 1
    return answer-aloc[0]

print(solution(22,6,8))
# print(solution(13,3,6))