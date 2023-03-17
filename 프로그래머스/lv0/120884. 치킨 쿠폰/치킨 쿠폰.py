def solution(chicken):
    coupon = chicken # 쿠폰
    answer = 0 # 총 서비스 키친 수
    while coupon >= 10:
        service = coupon // 10 # 서비스 치킨
        coupon = (coupon % 10) + service # 남은 쿠폰 + 서비스 쿠폰
        answer += service
    return answer