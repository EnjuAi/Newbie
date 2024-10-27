import re
from collections import Counter

# 데이터를 사용자로부터 입력받기
data = input("분석할 데이터를 입력하세요: ")

# 데이터셋 정의
dataset = [
    "김범수", "박원석", "임정수", "공하은", "김명주", "최하동", "김한백", "김나연", "윤여원", "이재윤", 
    "김유한", "문광덕", "김하은", "서동규", "이돈성", "안지호", "지준화", "허승혁", "김형준", "김진혁", "안겸"
]

# ']'와 공백 사이의 텍스트 추출하는 정규 표현식
pattern = r'\](.*?)(?=\s|$)'

# 패턴에 맞는 모든 텍스트 추출
matches = re.findall(pattern, data)

# 공백 값 제외
matches = [match for match in matches if match.strip()]

# '/'가 있는 경우 '/' 뒤의 값만 추출
matches = [match.split('/')[-1] for match in matches]

# 숫자 제거
matches = [re.sub(r'\d+', '', match) for match in matches]

# 카운트 계산
count = Counter(matches)

# 데이터셋과 비교하여 포함된 횟수 계산
dataset_count = {item.strip(): matches.count(item.strip()) for item in dataset}

# 결과 출력
print("\n카운트 결과:")
for key, value in count.items():
    print(f"'{key.strip()}': {value}")

print("\n데이터셋 내 포함 횟수:")
for key, value in dataset_count.items():
    print(f"{key}: {value}")
