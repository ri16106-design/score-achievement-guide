
# 1. 과목별 점수 데이터
scores = {
    "과학": 45,
    "영어": 98,
    "수학": 92,
    "국어": 85,
    "사회": 72
}

# 2. 이름 입력
name = input("이름을 입력하세요: ")

# 3. 과목 선택
subjects = ["과학", "영어", "수학", "국어", "사회"]

print("\n===== 과목 선택 =====")

for i in range(len(subjects)):
    print(i + 1, ".", subjects[i])

choice = int(input("과목 번호를 선택하세요: "))

# 4. 결과 확인 함수
def check_score(name, subject):
    score = scores[subject]

    # 성취도 확인
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "D"

    # 결과 출력
    print("\n===== 성적 확인 결과 =====")
    print("이름:", name)
    print("과목:", subject)
    print("점수:", score, "점")
    print("성취도:", grade)

    # 위험도 확인
    if score <= 50:
        risk = 2
        print("위험도 점수:", risk)
        print("안내 문자: 학습 주의! 해당 과목을 복습하세요.")
    else:
        risk = 0
        print("위험도 점수:", risk)
        print("안내 문자: 좋은 학습 상태를 유지하세요!")

# 5. 선택한 과목의 결과 출력
if 1 <= choice <= 5:
    selected_subject = subjects[choice - 1]
    check_score(name, selected_subject)
else:
    print("잘못된 번호입니다.")
