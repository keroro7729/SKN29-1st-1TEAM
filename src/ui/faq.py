from __future__ import annotations

import streamlit as st


def render_faq_page(start, end, road_name: str) -> None:
    _ = (start, end, road_name)

    # 🎨 카드 스타일
    st.markdown(
        """
<style>
.faq-box {
    padding: 16px;
    border-radius: 12px;
    background-color: #f5f7fa;
    margin-bottom: 12px;
    line-height: 1.7;
}
</style>
""",
        unsafe_allow_html=True,
    )

    st.markdown("## ❓ FAQ 검색")
    st.caption("키워드를 입력하면 관련 질문만 확인할 수 있습니다.")

    # 🔍 검색창
    query = st.text_input("검색어를 입력하세요 (예: 데이터, 스트레스, 필터)")

    # 📚 FAQ 데이터
    faq_data = [
        {
            "category": "🖥 사용 방법",
            "q": "이 대시보드는 어떻게 사용하나요?",
            "a": """
<div class="faq-box">

👉 <b>사이드바에서 조건을 선택하면 결과가 자동 반영됩니다.</b><br><br>

- 원하는 카테고리 선택  
- 날짜 필터 설정  
- 그래프 자동 업데이트  

※ 화물차 사고 통계는 일부 필터 적용이 제한됩니다  

</div>
""",
        },
        {
            "category": "🖥 사용 방법",
            "q": "필터를 여러 개 선택하면 어떻게 되나요?",
            "a": """
<div class="faq-box">

👉 <b>선택한 모든 조건이 동시에 적용됩니다.</b><br><br>

- 예) 
- 2026-01-01 ~ 2026-01-31  
- 도로 선택: 전체
- 26년 1월 기간의 인천 전체 도로


</div>
""",
        },
        {
            "category": "🔄 문제 해결",
            "q": "그래프가 변경되지 않는 경우 어떻게 하나요?",
            "a": """
<div class="faq-box">

👉 <b>일시적인 로딩 지연일 수 있습니다.</b><br><br>

- 잠시 기다린 후 확인  
- 문제가 지속되면 새로고침(F5)  

</div>
""",
        },
        {
            "category": "📈 데이터 해석",
            "q": "스트레스 지수는 어떻게 해석하나요?",
            "a": """
<div class="faq-box">
 

👉 <b>운전자의 “체감 혼잡”이 큰 구간을 우선 식별하는 데 사용입니다.</b><br><br>

- 속도 저하(정체)
- 변동성(급가감속/흐름 불안정)
- 교통량 혼잡도를 시간 단위로 결합해 산출한 지표

</div>
""",
        },
        {
            "category": "📊 데이터",
            "q": "데이터는 어디서 수집했나요?",
            "a": """
<div class="faq-box">

👉 <b>인천광역시 공공데이터를 기반으로 수집했습니다.</b><br><br>

- 공공 데이터: 인천광역시_도로 교통량 통계
- 공공 데이터: 인천광역시_도로 통행속도 통계 조회 서비스
- 공공 데이터: 인천광역시_도로_위험
- 공공 데이터: 기상청_지상(종관, ASOS) 시간자료 조회서비스
- 동적 크롤링: 네이버 뉴스 [인천, 교통사고, 사망] 키워드 데이터 수집

</div>
""",
        },
        {
            "category": "📊 데이터",
            "q": "데이터의 신뢰성은 어떻게 확보했나요?",
            "a": """
<div class="faq-box">

👉 <b>전처리를 통해 데이터 품질을 확보했습니다.</b><br><br>

- 결측치 제거  
- 이상치 처리  
- 데이터 정합성 검증  

</div>
""",
        },
        {
            "category": "⚙️ 시스템",
            "q": "데이터는 실시간인가요?",
            "a": """
<div class="faq-box">

👉 <b>26년 1월부터 3월 30일까지 수집된 데이터입니다.
   실시간 도로 KPI는 최근 1시간 구간의 데이터입니다.</b>

</div>
""",
        },
        {
            "category": "⚙️ 시스템",
            "q": "데이터 업데이트는 얼마나 자주 되나요?",
            "a": """
<div class="faq-box">

👉 <b>데이터셋 갱신 주기에 따라 업데이트됩니다.</b><br><br>

- 현재는 정적 데이터 기반으로 제공됩니다  

</div>
""",
        },
        {
            "category": "🚀 활용",
            "q": "이 대시보드를 통해 무엇을 할 수 있나요?",
            "a": """
<div class="faq-box">

👉 <b>데이터 기반 의사결정을 지원합니다.</b><br><br>

- 예)
- 교통 혼잡 시간대 예측  
- 사고 위험 구간 파악  
- 도로 개선 우선순위 설정  

</div>
""",
        },
    ]

    # 🔍 필터링
    if query:
        q = query.lower()
        filtered_faq = [
            item for item in faq_data if q in item["q"].lower() or q in item["a"].lower()
        ]
    else:
        filtered_faq = faq_data

    # 📦 출력
    current_category = ""
    for item in filtered_faq:
        if item["category"] != current_category:
            st.markdown(f"### {item['category']}")
            current_category = item["category"]

        with st.expander(f"Q. {item['q']}"):
            st.markdown(item["a"], unsafe_allow_html=True)

    # 📩 안내문
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.divider()
    st.info("시스템 이용 관련 추가 문의사항은 관리자 메일로 연락 주세요.")