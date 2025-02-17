def solution(players, m, k):
    answer = 0
    server = [] 
    
    for player in players:

        server = [s - 1 for s in server]
        server = [s for s in server if s > 0]


        required_servers = (player) // m
        
        additional_servers = max(0, required_servers - len(server))  


        for _ in range(additional_servers):
            server.append(k) 
            answer += 1
        #rint(player, server, answer)
    return answer
