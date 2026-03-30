# 🚗 인천광역시 도로 가이드

> 🔵 데이터로 교통을 이해하고, 🔴 문제를 발견하며, 🟢 개선 방향을 제시한다


<br><br>

---

<br><br>


## 🦸 Hero

> 프로젝트 핵심 요약

<br>

인천광역시 도로 데이터를 기반으로  
**교통 패턴, 사고 요인, 공항 유입 흐름, 운전자 스트레스 지수**를 분석하여  

<br>

👉 **개선이 필요한 도로와 정책 인사이트 도출**

<br><br>

---

<br><br>


## 🖼 Visualization Preview

> 주요 결과를 한눈에 확인

<br>

### 📍 교통 패턴

<br>

<p align="center">
  <img src="./assets/pattern.png" width="700"/>
</p>

<br><br>

### 📍 사고 분석

<br>

<p align="center">
  <img src="./assets/accident.png" width="700"/>
</p>

<br><br>

### 📍 공항 흐름

<br>

<p align="center">
  <img src="./assets/airport.png" width="700"/>
</p>

<br><br>

### 📍 스트레스 지수

<br>

<p align="center">
  <img src="./assets/stress.png" width="700"/>
</p>

<br><br>

---

<br><br>


## 📊 Key Signals

> 핵심 인사이트 요약

<br>

- 🌧 **비 오는 출근 시간 → 교통량 +30% 증가**

- 🚨 **사고 발생 = 날씨 + 시간 영향 큼**

- ✈️ **공항 이동 → 특정 도로 집중**

- 😡 **고스트레스 도로 존재 → 개선 필요**

<br><br>

---

<br><br>


## 🌐 Project Route

> 분석 구조 한눈에 보기

<br>

| 분석 영역 | 설명 |
|----------|------|
| 🔵 패턴 분석 | 시간 / 요일 / 날씨 기반 |
| 🔴 사고 분석 | 사고 영향 요인 |
| ✈️ 공항 흐름 | 유입 경로 분석 |
| 😡 스트레스 | 도로 위험도 평가 |

<br><br>

---

<br><br>


## 🗂 Data Route

> 데이터 흐름 설명

<br>

- 📁 **출처**  
  → 인천광역시 공공데이터

<br>

- 🔄 **전처리**  
  → 결측치 제거 / 시간 변환 / 날씨 병합

<br>

- 📌 **Feature**  
  → 시간 / 요일 / 날씨 / 교통량 / 사고

<br><br>

---

<br><br>


## 🧩 ERD 구조도

> 데이터 구조

<br>

<p align="center">
  <img src="https://github.com/user-attachments/assets/a8525877-28e9-4cbc-88c1-e53c29a7134d" width="700"/>
</p>

<br><br>

---

<br><br>


## 🛠 Tech Stack

> 사용 기술

<br>

### 💻 Language & Data

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

<br>

### 🗄 Database

<br>

![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

<br>

### 📊 Visualization / App

<br>

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

<br>

### ⚙️ Tools

<br>

![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

<br><br>

---

<br><br>


## 👥 Team Route

<br>

<p align="center">
  <img src="https://github.com/user-attachments/assets/289160b5-c928-49a7-81ab-8ccc4b3aaeba" width="800"/>
</p>

<br>

> 역할 분담

<br>

| 이름 | 역할 | 담당 |
|------|------|------|
| 진욱 | ✈️ 분석 | 공항 흐름 |
| 은진 | 😡 분석 | 스트레스 지수 |
| 지현 | 🔵 분석 | 패턴 분석 |
| 동윤 | 🔴 분석 | 사고 분석 |

<br><br>

---

<br><br>


## 👤 팀원 소개 / 역할

> 개인 기여 상세

<br>

### 🧑‍💻 지현
- 교통 패턴 분석  
- 시계열 데이터 처리

<br>

### 🧑‍💻 동윤
- 사고 영향도 분석  
- 상관관계 크롤링  

<br>

### 🧑‍💻 진욱
- 공항 유입 경로 분석  
- 공간 데이터 시각화  

<br>

### 🧑‍💻 은진
- 스트레스 지수 설계  
- 개선 도로 도출  

<br><br>

---

<br><br>


## ⚡ Quick Start

> 실행 방법

<br>

```bash
git clone https://github.com/your-repo.git
cd your-repo
pip install -r requirements.txt
jupyter notebook
