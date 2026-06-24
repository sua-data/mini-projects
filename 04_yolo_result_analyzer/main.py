import pandas as pd
import matplotlib.pyplot as plt

# 한글 폰트 설정 - Windows
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# YOLO 탐지 결과 데이터 불러오기
df = pd.read_csv("yolo_result_sample.csv")

print("=== YOLO 탐지 결과 원본 데이터 ===")
print(df)

# 클래스별 탐지 개수
class_counts = df["class_name"].value_counts().reset_index()
class_counts.columns = ["class_name", "detection_count"]

# 클래스별 평균 confidence
confidence_mean = df.groupby("class_name")["confidence"].mean().reset_index()
confidence_mean.columns = ["class_name", "avg_confidence"]

# 결과 병합
result_df = pd.merge(class_counts, confidence_mean, on="class_name")
result_df = result_df.sort_values(by="detection_count", ascending=False)

print("\n=== 클래스별 탐지 분석 결과 ===")
print(result_df)

# 결과 저장
result_df.to_csv("yolo_analysis_result.csv", index=False, encoding="utf-8-sig")

# 클래스별 탐지 개수 그래프
plt.figure(figsize=(8, 5))
plt.bar(result_df["class_name"], result_df["detection_count"])
plt.title("클래스별 탐지 개수")
plt.xlabel("클래스")
plt.ylabel("탐지 개수")
plt.tight_layout()
plt.savefig("class_count_chart.png", dpi=300)
plt.show()

# 클래스별 평균 confidence 그래프
plt.figure(figsize=(8, 5))
plt.bar(result_df["class_name"], result_df["avg_confidence"])
plt.title("클래스별 평균 Confidence")
plt.xlabel("클래스")
plt.ylabel("평균 Confidence")
plt.ylim(0, 1)
plt.tight_layout()
plt.savefig("confidence_chart.png", dpi=300)
plt.show()