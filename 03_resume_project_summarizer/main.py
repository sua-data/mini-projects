import pandas as pd

# 프로젝트 정보 데이터 불러오기
df = pd.read_csv("project_info_sample.csv")

print("=== 프로젝트 정보 원본 데이터 ===")
print(df)

# README/이력서용 문장 생성 함수
def make_summary(row):
    project_name = row["project_name"]
    role = row["role"]
    tech_stack = row["tech_stack"]
    main_task = row["main_task"]
    result = row["result"]

    summary = f"""
## {project_name}

- 역할: {role}
- 사용 기술: {tech_stack}
- 주요 수행 내용: {main_task}
- 결과: {result}

### 이력서용 요약 문장
{project_name} 프로젝트에서 {role} 역할을 맡아 {main_task}를 수행했습니다. {tech_stack}을 활용했으며, 최종적으로 {result}했습니다.
"""
    return summary.strip()

# 프로젝트별 요약 생성
summaries = []

for _, row in df.iterrows():
    summaries.append(make_summary(row))

# Markdown 파일로 저장
output_text = "\n\n---\n\n".join(summaries)

with open("project_summary.md", "w", encoding="utf-8") as file:
    file.write(output_text)

print("\n=== 생성된 프로젝트 요약 ===")
print(output_text)

print("\nproject_summary.md 파일이 생성되었습니다.")