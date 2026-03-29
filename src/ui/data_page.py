import streamlit as st
from service import sample_service
import pandas as pd

def render_data_page():
    st.dataframe(sample_service.select_all())