import pandas as pd
import streamlit as st
from db.db_client import Client
import db.queries as queries

DEFAULT_TTL = 60 * 10

@st.cache_resource
def get_client():
    return Client()

@st.cache_data(ttl=DEFAULT_TTL)
def select_all():
    query = queries.select_all_traffic()
    columns, rows = get_client().select(query, ())
    return pd.DataFrame(data=rows, columns=columns)