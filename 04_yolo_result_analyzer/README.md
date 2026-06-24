# YOLO Result Analyzer

YOLO 객체 탐지 결과를 분석하는 미니 프로젝트입니다.  
탐지 결과 데이터를 기반으로 클래스별 탐지 개수와 평균 confidence를 계산하고, 결과를 CSV와 그래프로 저장합니다.

## 프로젝트 목적

YOLO 모델을 실행한 뒤 결과를 단순히 확인하는 것에서 끝내지 않고, 탐지 결과를 정리하여 클래스별 탐지 경향을 분석하는 것이 목적입니다.

## 사용 데이터

`yolo_result_sample.csv` 파일을 사용했습니다.

| 컬럼명 | 설명 |
|---|---|
| image_name | 이미지 파일명 |
| class_name | 탐지된 객체 클래스 |
| confidence | 탐지 신뢰도 |
| x_center | 바운딩 박스 중심 x좌표 |
| y_center | 바운딩 박스 중심 y좌표 |
| width | 바운딩 박스 너비 |
| height | 바운딩 박스 높이 |

## 주요 기능

- YOLO 탐지 결과 CSV 불러오기
- 클래스별 탐지 개수 계산
- 클래스별 평균 confidence 계산
- 분석 결과 CSV 저장
- 클래스별 탐지 개수 그래프 생성
- 클래스별 평균 confidence 그래프 생성

## 사용 기술

- Python
- pandas
- matplotlib
- CSV 데이터 처리

## 실행 방법

```bash
python main.py