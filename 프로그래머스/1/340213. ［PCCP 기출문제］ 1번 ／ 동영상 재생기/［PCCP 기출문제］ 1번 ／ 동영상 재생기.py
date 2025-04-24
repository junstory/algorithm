def timeAdd(t):
    h = int(t[:2])
    m = int(t[3:])
    m += 10
    if m>60:
        h += 1
        m %= 60
    return f"{h:0>2}:{m:0>2}"
def timeSub(t):
    h = int(t[:2])
    m = int(t[3:])
    m -= 10
    if m<0:
        h -= 1
        m += 60
    if h < 0:
        h = m = 0
    return f"{h:0>2}:{m:0>2}"
    
    
def solution(video_len, pos, op_start, op_end, commands):
    
    for cmd in commands:
        if op_start <= pos <= op_end:
            pos = op_end
        #print(1,pos)
        if cmd == "next":
            pos = timeAdd(pos)
        elif cmd == "prev":
            pos = timeSub(pos)
        #print(2,pos)
        if op_start <= pos <= op_end:
            pos = op_end
        if pos > video_len:
            pos = video_len
    
    answer = pos
    return answer