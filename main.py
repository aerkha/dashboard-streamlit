import pandas as pd
import streamlit as st
import plotly_express as px
from numerize.numerize import numerize

st.set_page_config(
    page_title='Marketing Program Review',
    layout='wide',
    initial_sidebar_state='collapsed'
)

@st.cache_data
def get_data():
    df = pd.read_csv('Marketing_Database.csv')
    return df

df = get_data()

header_left, header_mid, header_right = st.columns([1, 2, 1], gap='large')

# dashboard title

with header_mid:
    st.title("CMM Dashboard")

# side filters

with st.sidebar:
    Campaign_filter = st.multiselect(label='Select Campaign',
                                     options=df['Campaign'].unique(),
                                     default=df['Campaign'].unique()
                                     )
    Stage_filter = st.multiselect(label='Select Stage',
                                  options=df['Stage'].unique(),
                                  default=df['Stage'].unique()
                                  )
    Group_filter = st.multiselect(label='Select Group',
                                  options=df['New Group'].unique(),
                                  default=df['New Group'].unique()
                                  )