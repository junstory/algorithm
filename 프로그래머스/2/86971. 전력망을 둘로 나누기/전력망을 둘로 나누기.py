def findParent(n, arr):
    if n != arr[n]:
        arr[n] = findParent(arr[n],arr)
    return arr[n]

def union(a,b, arr):
    ra = findParent(a, arr)
    rb = findParent(b, arr)
    if ra == rb:
        return arr
    
    if ra > rb:
        arr[ra] = rb
    else:
        arr[rb] = ra
    return arr
            
    
    
def solution(n, wires):
    answer = n
    for i in range(len(wires)):
        test_wire = wires[::]
        test_wire.pop(i)
        arr = [i for i in range(n+1)]
        for a, b in test_wire:
            arr = union(a,b,arr)
        
        wire_set = set()
        a = 0
        b = 0
        for j in range(1, n+1):
            arr[j] = findParent(j, arr)
        arr = arr[1:]
        for wire in arr:
            if wire in wire_set:
                continue
            elif (wire not in wire_set) and (not wire_set):
                a = arr.count(wire)
                wire_set.add(wire)
            elif wire not in wire_set and wire_set:
                b = arr.count(wire)
                wire_set.add(wire)
            
            
        #print(test_wire, arr, abs(a-b))
        answer = min(answer, abs(a-b))
            
        
        
    return answer