def solution(participant, completion):
    players = set(participant)
    counter = dict()
    for player in participant:
        if player not in counter:
            counter[player] = 1
        else:
            counter[player] += 1
    
    for player in completion:
        counter[player] -= 1
    
    for player in players:
        if counter[player] > 0:
            answer = player
            break
        
    return answer