import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# 한글 폰트 설정 - Windows
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# 뉴스 데이터 불러오기
df = pd.read_csv("news_sample.csv")

# 분석할 키워드 목록
keywords = [
    "금리", "시장", "삼성전자", "반도체", "환율",
    "수출", "증시", "AI", "글로벌", "경제", "정책", "물가"
]

# 제목에서 키워드 빈도 계산
keyword_counts = Counter()

for title in df["title"]:
    for keyword in keywords:
        if keyword in title:
            keyword_counts[keyword] += 1

# 결과를 DataFrame으로 변환
result_df = pd.DataFrame(
    keyword_counts.items(),
    columns=["keyword", "count"]
).sort_values(by="count", ascending=False)

print("=== 뉴스 키워드 빈도 분석 결과 ===")
print(result_df)

# 결과 저장
result_df.to_csv("keyword_result.csv", index=False, encoding="utf-8-sig")

# 시각화
plt.figure(figsize=(8, 5))
plt.bar(result_df["keyword"], result_df["count"])
plt.title("뉴스 키워드 빈도 분석")
plt.xlabel("키워드")
plt.ylabel("빈도")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("keyword_chart.png", dpi=300)
plt.show()