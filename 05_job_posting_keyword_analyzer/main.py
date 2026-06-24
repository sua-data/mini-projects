import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# 한글 폰트 설정 - Windows
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# 채용공고 데이터 불러오기
df = pd.read_csv("job_postings_sample.csv")

print("=== 채용공고 원본 데이터 ===")
print(df)

# 분석할 기술스택 키워드
tech_keywords = [
    "Python", "SQL", "FastAPI", "MySQL", "MariaDB",
    "Elasticsearch", "Docker", "React", "JavaScript",
    "HTML", "CSS", "pandas", "scikit-learn", "Git"
]

# 제목 + 설명 합쳐서 분석
keyword_counts = Counter()

for _, row in df.iterrows():
    text = f"{row['job_title']} {row['description']}"
    for keyword in tech_keywords:
        if keyword.lower() in text.lower():
            keyword_counts[keyword] += 1

# 결과 DataFrame 생성
result_df = pd.DataFrame(
    keyword_counts.items(),
    columns=["tech_keyword", "count"]
).sort_values(by="count", ascending=False)

print("\n=== 기술스택 키워드 분석 결과 ===")
print(result_df)

# 결과 저장
result_df.to_csv("job_keyword_result.csv", index=False, encoding="utf-8-sig")

# 그래프 생성
plt.figure(figsize=(9, 5))
plt.bar(result_df["tech_keyword"], result_df["count"])
plt.title("채용공고 기술스택 키워드 빈도")
plt.xlabel("기술스택")
plt.ylabel("등장 빈도")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("job_keyword_chart.png", dpi=300)
plt.show()