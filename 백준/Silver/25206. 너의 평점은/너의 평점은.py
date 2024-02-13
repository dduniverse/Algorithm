avg_dict = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

major_score = 0 # 전공과목별 (학점 × 과목평점)의 합
sum_score = 0 # 학점의 총합

for i in range(20):
    _, score, grade = input().split() # 과목명, 학점, 등급
    
    if grade == 'P': # 등급이 P인 과목은 계산에서 제외
        continue
    else:
        major_score += float(score) * avg_dict[grade]
        sum_score += float(score)

print(major_score / sum_score) # 전공 평점 출력