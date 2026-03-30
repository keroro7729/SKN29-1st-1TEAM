# 🚗 인천광역시 도로 가이드

> 🔵 데이터로 교통을 이해하고, 🔴 문제를 발견하며, 🟢 개선 방향을 제시한다


---


## 🦸 Hero

> 프로젝트 핵심 요약

인천광역시 도로 데이터를 기반으로  
**교통 패턴, 사고 요인, 공항 유입 흐름, 운전자 스트레스 지수**를 분석하여  
👉 **개선이 필요한 도로와 정책 인사이트 도출**

---

## 🖼 Visualization Preview

> 주요 결과를 한눈에 확인

### 📍 교통 패턴
![pattern](./assets/pattern.png)

### 📍 사고 분석
![accident](./assets/accident.png)

### 📍 공항 흐름
![airport](./assets/airport.png)

### 📍 스트레스 지수
![stress](./assets/stress.png)

---

## 📊 Key Signals

> 핵심 인사이트 요약

- 🌧 **비 오는 출근 시간 → 교통량 +30% 증가**
- 🚨 **사고 발생 = 날씨 + 시간 영향 큼**
- ✈️ **공항 이동 → 특정 도로 집중**
- 😡 **고스트레스 도로 존재 → 개선 필요**

---

## 🌐 Project Route

> 분석 구조 한눈에 보기

| 분석 영역 | 설명 |
|----------|------|
| 🔵 패턴 분석 | 시간 / 요일 / 날씨 기반 |
| 🔴 사고 분석 | 사고 영향 요인 |
| ✈️ 공항 흐름 | 유입 경로 분석 |
| 😡 스트레스 | 도로 위험도 평가 |

---

## 🗂 Data Route

> 데이터 흐름 설명

- 📁 **출처**  
  → 인천광역시 공공데이터

- 🔄 **전처리**  
  → 결측치 제거 / 시간 변환 / 날씨 병합

- 📌 **Feature**  
  → 시간 / 요일 / 날씨 / 교통량 / 사고

---

## 🧩 ERD 구조도

> 데이터 구조

![ERD](https://github.com/keroro7729/SKN29-1st-1TEAM/issues/1)

---

## 🛠 Tech Stack

> 사용 기술

### 💻 Language & Data
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

### 🗄 Database
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

### 📊 Visualization / App
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

### ⚙️ Tools
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

---

## 👥 Team Route

> 역할 분담

| 이름 | 역할 | 담당 |
|------|------|------|
| 지현 | 🔵 분석 | 패턴 분석 |
| 동윤 | 🔴 분석 | 사고 분석 |
| 진욱 | ✈️ 분석 | 공항 흐름 |
| 은진 | 😡 분석 | 스트레스 지수 |

---

## 👤 팀원 소개 / 역할

> 개인 기여 상세

### 🧑‍💻 지현
- 교통 패턴 분석
- 시계열 데이터 처리

### 🧑‍💻 동윤
- 사고 영향도 분석
- 상관관계 크롤링

### 🧑‍💻 진욱
- 공항 유입 경로 분석
- 공간 데이터 시각화

### 🧑‍💻 은진
- 스트레스 지수 설계
- 개선 도로 도출

---

## ⚡ Quick Start

> 실행 방법

```bash
git clone https://github.com/your-repo.git
cd your-repo
pip install -r requirements.txt
jupyter notebook
