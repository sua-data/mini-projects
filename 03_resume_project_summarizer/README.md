# Resume Project Summarizer

프로젝트 경험을 이력서와 포트폴리오에 정리하기 위한 미니 프로젝트입니다.  
프로젝트명, 역할, 사용 기술, 주요 수행 내용, 결과를 CSV로 입력하면 Markdown 형식의 프로젝트 요약 문장을 생성합니다.

## 프로젝트 목적

프로젝트 경험을 매번 새로 작성하지 않고, 일정한 형식으로 정리할 수 있도록 자동화하는 것이 목적입니다.  
이력서, 포트폴리오 README, 발표 자료에 활용할 수 있는 프로젝트 설명 문장을 생성합니다.

## 사용 데이터

`project_info_sample.csv` 파일을 사용했습니다.

| 컬럼명 | 설명 |
|---|---|
| project_name | 프로젝트명 |
| role | 담당 역할 |
| tech_stack | 사용 기술 |
| main_task | 주요 수행 내용 |
| result | 프로젝트 결과 |

## 주요 기능

- 프로젝트 정보 CSV 불러오기
- 프로젝트별 역할, 기술, 수행 내용 정리
- 이력서용 요약 문장 자동 생성
- Markdown 파일로 저장

## 사용 기술

- Python
- pandas
- file I/O
- Markdown 텍스트 생성

## 실행 방법

```bash
python main.py