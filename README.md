<div align="center">

# 🛣️ Incheon Road Guide Visualization

### 인천광역시 도로 정보를 더 직관적으로 탐색하고 이해할 수 있도록 설계한 스마트시티형 시각화 프로젝트

<br>

![Status](https://img.shields.io/badge/status-active-22C55E?style=for-the-badge)
![Made with](https://img.shields.io/badge/made%20with-[사용기술]-0EA5E9?style=for-the-badge)
![Data](https://img.shields.io/badge/data-public%20data-FACC15?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-64748B?style=for-the-badge)

<br>

> **Visualizing the roads of Incheon, clearly and intuitively**  
> 도시의 길을 더 명확하게, 인천광역시 도로 가이드 시각화 프로젝트

<br>

![banner](./assets/banner.png)

</div>

---

## 📍 Project Route

**Incheon Road Guide Visualization**은  
인천광역시의 도로 정보를 보다 쉽게 탐색하고 이해할 수 있도록  
지도 기반 인터페이스와 시각화 요소를 활용해 구성한 프로젝트입니다.

복잡한 도로 구조와 주요 구간, 행정구역 또는 노선 중심의 정보를  
직관적인 방식으로 전달하는 것을 목표로 합니다.  
단순한 지도 표시를 넘어, 사용자가 **도로 흐름과 위치 관계를 빠르게 파악할 수 있는 가이드형 시각화 경험**을 제공합니다.

---

## 🚦 Key Signals

<table>
  <tr>
    <td width="33%">
      <h3>🗺️ Road Visualization</h3>
      <p>도로 구간, 주요 노선, 행정구역 정보를 시각적으로 표현하여 빠른 이해를 돕습니다.</p>
    </td>
    <td width="33%">
      <h3>📌 Guide-Oriented UI</h3>
      <p>교통안내판과 경로 가이드에서 영감을 받은 인터페이스로 정보 탐색 흐름을 단순화했습니다.</p>
    </td>
    <td width="33%">
      <h3>🏙️ Smart City Perspective</h3>
      <p>도시 인프라와 공공데이터를 연결해 인천광역시 도로 체계를 디지털 대시보드처럼 보여줍니다.</p>
    </td>
  </tr>
</table>

---

## 🧭 Why This Project

이 프로젝트는 다음과 같은 문제의식에서 출발했습니다.

- 도로 정보는 많지만, 한눈에 이해하기 어려운 경우가 많습니다.
- 지도 데이터는 존재하지만, 사용자가 빠르게 길의 구조와 특징을 파악하기엔 불친절할 수 있습니다.
- 공공데이터와 시각화 기술을 결합하면 도시 이동 정보를 더 직관적으로 전달할 수 있습니다.

그래서 본 프로젝트는  
**“데이터를 보여주는 지도”**가 아니라,  
**“길을 읽게 해주는 가이드”**를 만드는 데 초점을 맞췄습니다.

---

## 🖥️ Visualization Preview

<table>
  <tr>
    <td align="center">
      <img src="./assets/preview-main.png" width="100%" alt="main preview" />
      <br />
      <sub>메인 지도 화면</sub>
    </td>
    <td align="center">
      <img src="./assets/preview-route.png" width="100%" alt="route preview" />
      <br />
      <sub>주요 도로 구간 강조 시각화</sub>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="./assets/preview-district.png" width="100%" alt="district preview" />
      <br />
      <sub>행정구역 기반 탐색 화면</sub>
    </td>
    <td align="center">
      <img src="./assets/preview-layer.png" width="100%" alt="layer preview" />
      <br />
      <sub>데이터 레이어 및 정보 패널</sub>
    </td>
  </tr>
</table>

> 실제 화면 캡처가 아직 없다면, 우선 목업 이미지나 지도 일부 캡처로 채워두는 것도 좋습니다.

---

## 🏗️ System Overview

```text
[Public Data / Geo Data]
          ↓
   [Data Processing]
          ↓
 [Map Rendering Engine]
          ↓
 [Guide Visualization UI]
          ↓
   [User Interaction]
