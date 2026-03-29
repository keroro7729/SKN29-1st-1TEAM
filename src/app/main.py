import streamlit as st

from ui.data_page import render_data_page

st.set_page_config('인천 도로 분석 페이지')

render_data_page()