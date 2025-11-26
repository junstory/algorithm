import math
def solution(fees, records):
    answer = []
    base_time, base_price, unit_time, unit_price = fees
    def minute(time):
        h = int(time[:2])
        m = int(time[3:])
        
        return h*60 + m
    
    record_in = dict()
    pricing = dict()
    parking_sum = dict()
    for s in records:
        time, number, status = s.split()
        t_t = minute(time)
        
        if status == "IN":
            record_in[number] = t_t
        else:
            parking_time = t_t - record_in[number]
            parking_sum[number] = parking_sum.get(number,0) + parking_time
            del record_in[number]
    #미출차 계산
    for number in record_in.keys():
        parking_time = 1439 -record_in[number]
        parking_sum[number] = parking_sum.get(number,0) + parking_time
    #출차 계산
    for number in parking_sum.keys():
        parking_time = parking_sum[number]
        parking_price = base_price if parking_time <= base_time else base_price + math.ceil((parking_time-base_time)/ unit_time)*unit_price
        pricing[number] = pricing.get(number,0) + parking_price
    #번호순으로 저장
    for number in sorted(list(pricing.keys())):
        answer.append(pricing[number])
    
    return answer