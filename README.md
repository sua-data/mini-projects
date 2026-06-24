# mini-projects

Python, 데이터 분석, 머신러닝, YOLO 실습을 기반으로 진행한 개인 미니 프로젝트 모음입니다.
각 프로젝트는 작은 문제를 직접 정의하고, 데이터를 처리하거나 조건을 분석하여 결과를 도출하는 방식으로 구성했습니다.

## 프로젝트 목록

| No. | 프로젝트명                             | 설명                               | 주요 기술                      |
| --- | --------------------------------- | -------------------------------- | -------------------------- |
| 01  | Stomach Friendly Food Recommender | 위에 부담이 적은 음식 추천 프로그램             | Python, pandas             |
| 02  | News Keyword Analyzer             | 뉴스 제목/본문 기반 키워드 빈도 분석            | Python, pandas, matplotlib |
| 03  | Resume Project Summarizer         | 프로젝트 경험을 이력서/README 문장으로 정리하는 도구 | Python, file I/O        |
| 04  | YOLO Result Analyzer              | YOLO 탐지 결과를 클래스별로 분석하는 도구        | Python, pandas, matplotlib |
| 05  | Job Posting Keyword Analyzer      | 채용공고에서 주요 기술스택 키워드를 분석하는 도구 | Python, pandas, matplotlib  |

---

## 01. Stomach Friendly Food Recommender

위염 증상이 있거나 자극적인 음식을 피해야 하는 상황에서 사용할 수 있는 음식 추천 프로그램입니다.
음식 데이터를 기반으로 맵기, 기름짐, 밀가루 포함 여부 등을 조건으로 필터링하여 비교적 부담이 적은 음식을 추천합니다.

### 주요 기능

* 음식 데이터 불러오기
* 사용자 조건에 따른 음식 필터링
* 추천 음식 목록 출력
* 음식별 특징 정리

### 사용 기술

* Python
* pandas
* CSV 데이터 처리

---

## 02. News Keyword Analyzer

뉴스 데이터에서 자주 등장하는 키워드를 추출하고 빈도를 분석하는 미니 프로젝트입니다.
경제 뉴스 분석 서비스 프로젝트인 DATA와 연결되는 기초 분석 프로젝트로, 뉴스 제목 또는 본문 데이터를 기반으로 키워드 흐름을 확인합니다.

### 주요 기능

* 뉴스 데이터 불러오기
* 키워드 빈도 계산
* 상위 키워드 추출
* 키워드 빈도 시각화

### 사용 기술

* Python
* pandas
* collections.Counter
* matplotlib

---

## 03. Resume Project Summarizer

프로젝트 경험을 이력서나 포트폴리오에 정리할 때 사용할 수 있는 문장 생성 도구입니다.
프로젝트명, 역할, 사용 기술, 주요 구현 내용을 입력하면 README 또는 이력서에 사용할 수 있는 형식으로 정리합니다.

### 주요 기능

* 프로젝트 정보 입력
* 기술 스택 분류
* 역할 및 구현 내용 정리
* Markdown 형식 문장 생성

### 사용 기술

* Python
* dictionary
* list
* file I/O
* Markdown 텍스트 생성

---

## 04. YOLO Result Analyzer

YOLO 객체 탐지 결과를 분석하는 미니 프로젝트입니다.
탐지 결과 파일을 불러와 클래스별 탐지 개수, 평균 confidence, 탐지 비율 등을 계산합니다.

### 주요 기능

* YOLO 탐지 결과 데이터 불러오기
* 클래스별 탐지 개수 계산
* 평균 confidence 계산
* 결과 표 및 그래프 생성

### 사용 기술

* Python
* pandas
* matplotlib
* YOLO result data

---

## 05. Job Posting Keyword Analyzer

채용공고 데이터를 기반으로 주요 기술스택 키워드를 분석하는 프로젝트입니다.  
공고 제목과 직무 설명에서 Python, SQL, FastAPI, React, Docker 등 개발·데이터 직무에서 자주 요구되는 기술 키워드의 등장 빈도를 확인합니다.

### 주요 기능

* 채용공고 데이터 입력
* 기술스택 키워드 빈도 계산
* 직무별 요구 기술 비교
* 기술 키워드 빈도 그래프 생성

### 사용 기술

* Python
* pandas
* matplotlib
* CSV 데이터 처리

---

## 폴더 구조

```text
mini-projects/
├─ README.md
├─ 01_stomach_friendly_food_recommender/
├─ 02_news_keyword_analyzer/
├─ 03_resume_project_summarizer/
├─ 04_yolo_result_analyzer/
└─ 05_hardness_profile_analyzer/
```

---

## 목표

이 레포지토리는 수업 및 개인 학습 과정에서 배운 내용을 작은 단위의 프로젝트로 정리하기 위한 공간입니다.
각 프로젝트를 통해 Python 기초 문법, 데이터 처리, 시각화, 파일 입출력, 머신러닝 및 객체 탐지 결과 분석 역량을 정리하는 것을 목표로 합니다.
