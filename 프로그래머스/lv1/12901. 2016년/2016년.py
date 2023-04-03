import datetime

def solution(a, b):
    weekly = {0:'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}
    weekday = datetime.date(2016, a, b).weekday()
    return weekly[weekday]