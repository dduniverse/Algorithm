from datetime import datetime
import math

def solution(fees, records):
    answer = {record.split()[1]:0 for record in records}
    car = {}
    for record in records:
        time, car_num, inout = record.split()

        if inout == 'IN':
            car[car_num] = datetime.strptime(time,"%H:%M")
        else:
            pay = str(datetime.strptime(time,"%H:%M") - car[car_num])
            pay = int(pay.split(':')[0]) * 60 + int(pay.split(':')[1])
            answer[car_num] += pay
            del car[car_num]

    if len(car) > 0 :
        for i in car:
            pay = str(datetime.strptime('23:59',"%H:%M") - car[i])
            pay = int(pay.split(':')[0]) * 60 + int(pay.split(':')[1])
            answer[i] += pay

    answer = sorted(answer.items())
    for i in range(len(answer)):
        if answer[i][1] <= fees[0]:
            answer[i] = fees[1]
        else:
            answer[i] = fees[1] + math.ceil((answer[i][1] - fees[0])/fees[2]) * fees[3]

    return answer