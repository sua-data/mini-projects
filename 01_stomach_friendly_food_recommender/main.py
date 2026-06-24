import pandas as pd

# 음식 데이터 불러오기
df = pd.read_csv("food_sample.csv")

# 문자열 True/False를 실제 boolean으로 변환
bool_columns = ["spicy", "greasy", "contains_flour", "contains_caffeine"]

for column in bool_columns:
    df[column] = df[column].astype(str).str.lower().map({
        "true": True,
        "false": False
    })

print("=== 음식 데이터 ===")
print(df)

# 위에 부담이 적은 음식 조건
recommended_df = df[
    (df["spicy"] == False) &
    (df["greasy"] == False) &
    (df["contains_flour"] == False) &
    (df["contains_caffeine"] == False)
]

# 추천 결과 정리
result_df = recommended_df[["food_name", "category", "description"]]

print("\n=== 위에 부담이 적은 음식 추천 결과 ===")
print(result_df)

# 결과 저장
result_df.to_csv("food_recommendation_result.csv", index=False, encoding="utf-8-sig")

print("\nfood_recommendation_result.csv 파일이 생성되었습니다.")