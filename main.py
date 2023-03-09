import pandas as pd
import streamlit as st
#import plotly_express as px
from numerize.numerize import numerize

st.set_page_config(
    page_title='Marketing Program Review',
    layout='wide',
    initial_sidebar_state='collapsed'
)

@st.cache_data
def get_data():
    df = pd.read_csv('https://github.com/aerkha/isatb2b/blob/main/Marketing_Database.csv')
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

df1 = df.query('campaign == @Campaign_filter & stage == @Stage_filter & group == @Group_filter')

total_oppty = int(df1['SF Opportunity ID'].unique().count())
total_rev = float(df1['Revenue'].sum())
total_rev2023 = float(df1['Rev 2023'].sum())
total_accounts = int(df1['Account Name'].unique().count())


total1,total2,total3,total4 = st.columns(4,gap='large')

with total1:
    st.image('<a href="https://www.flaticon.com/free-icons/opportunity" title="opportunity icons">Opportunity icons created by iconixar - Flaticon</a>',use_column_width='Auto')
    st.metric(label = 'Total Oppty', value= numerize(total_oppty))
    
with total2:
    st.image('<a href="https://www.flaticon.com/free-icons/money" title="money icons">Money icons created by turkkub - Flaticon</a>',use_column_width='Auto')
    st.metric(label='Total Revenue (MRC+OTC)', value=numerize(total_rev))
    
with total3:
    st.image('<a href="https://www.flaticon.com/free-icons/piggy-bank" title="piggy bank icons">Piggy bank icons created by Freepik - Flaticon</a>',use_column_width='Auto')
    st.metric(label= 'Total Est. Rev 2023',value=numerize(total_rev2023))

with total4:
    st.image('<a href="https://www.flaticon.com/free-icons/work" title="work icons">Work icons created by geotatah - Flaticon</a>',use_column_width='Auto')
    st.metric(label='Total Customers',value=numerize(total_accounts))
    


