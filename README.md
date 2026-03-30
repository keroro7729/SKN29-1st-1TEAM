# 🛣️ 인천 로드 인사이트 (Incheon Road Insight)
> **데이터로 설계하는 스마트 도로 이용 가이드 및 안전 최적화 분석**

![Header Image](https://capsule-render.vercel.app/render?type=waving&color=auto&height=200&section=header&text=Incheon%20Road%20Analysis&fontSize=70)

## 🛠 Tech Stack
<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=Pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white"/>
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=Plotly&logoColor=white"/>
  <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=Git&logoColor=white"/>
</p>

---

## 📌 프로젝트 소개
인천은 대한민국 물류의 중심지이자 관문 도시입니다. 본 프로젝트는 산재된 공공데이터를 통합 분석하여 운전자에게 실질적인 **'도로 이용 가이드'**를 제공하고, **운전자 스트레스 지수**를 통해 개선이 필요한 도로를 제안합니다.

### 🔍 핵심 분석 내용
* **📅 요일/시간대별 패턴:** 상습 정체 구간의 시간적 흐름 분석
* **🌦️ 날씨별 사고 상관관계:** 강수/안개 등 기상 변화에 따른 위험도 수치화
* **✈️ 인천공항 흐름 분석:** 영종/인천대교 및 배후 도로 물류 최적화
* **😫 스트레스 지수 산출:** 정체 빈도와 사고량을 결합한 도로 위험도 평가

---

## 📊 분석 결과 샘플
| 구별 화물차 사고 비중 | 시간대별 정체 패턴 |
| :---: | :---: |
| ![그래프1_이미지주소](https://via.placeholder.com/400x250) | ![그래프2_이미지주소](https://via.placeholder.com/400x250) |

---

## 📂 프로젝트 구조
```text
├── data/               # 수집된 데이터 (CSV, JSON)
├── notebooks/          # 분석 과정 (Jupyter Notebook)
├── src/                # DB 연동 및 크롤링 스크립트
└── README.md           # 프로젝트 가이드