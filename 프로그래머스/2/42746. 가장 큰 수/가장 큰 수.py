
def solution(numbers):
    answer = ''
    li = []
    li = list(map(str, numbers))
    li.sort(reverse = True, key = lambda x : x*3)
    #print(li)
    for i in li:
        answer += "".join(i)
    answer = str(int(answer))
    return answer