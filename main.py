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
                                  options=df['New_Group'].unique(),
                                  default=df['New_Group'].unique()
                                  )

df1 = df.query('Campaign == @Campaign_filter and Stage == @Stage_filter and New_Group == @Group_filter')

df_oppty = pd.DataFrame(df1['SF_Opportunity_Id'].value_counts())
df_ca = pd.DataFrame(df1['Account_Name'].value_counts())

total_oppty = int(df_oppty.count())
total_rev = float(df1['Rev'].sum())
total_rev2023 = float(df1['Rev_2023'].sum())
total_accounts = int(df_ca.count())

total1, total2, total3, total4 = st.columns(4, gap='large')

with total1:
    st.image('Image/opportunity.png',use_column_width='auto')
    st.metric(label='Total Oppty', value=numerize(total_oppty))

with total2:
    st.image('Image/revenue.png',use_column_width='auto')
    st.metric(label='Total Revenue (MRC+OTC)', value=numerize(total_rev))

with total3:
    st.image('Image/rev2023.png',use_column_width='auto')
    st.metric(label='Total Est. Rev 2023', value=numerize(total_rev2023))

with total4:
    st.image('Image/account.png',use_column_width='auto')
    st.metric(label='Total Customers', value=numerize(total_accounts))

Q1,Q2 = st.columns(2)

with Q1:
    df2 = df1.groupby(by = ['Campaign']).sum()['Rev'].reset_index()
    df2['Rev'] =round(df2['Rev'] ,2)
    fig_rev_by_campaign = px.bar(df2,
                            x='Campaign',
                            y='Rev',
                            title='<b>Revenue (OTC MRC)</b>')
    fig_rev_by_campaign.update_layout(title = {'x' : 0.5},
                                    plot_bgcolor = "rgba(0,0,0,0)",
                                    xaxis =(dict(showgrid = False)),
                                    yaxis =(dict(showgrid = False)))
    st.plotly_chart(fig_rev_by_campaign,use_container_width=True)

with Q2:
    df3 = df1.groupby(by=['Campaign']).sum()['Rev_2023'].reset_index()
    df3['Rev_2023'] = round(df3['Rev_2023'], 2)
    fig_rev23_by_campaign = px.bar(df3,
                                 x='Campaign',
                                 y='Rev_2023',
                                 title='<b>Est. Revenue 2023</b>')
    fig_rev23_by_campaign.update_layout(title={'x': 0.5},
                                      plot_bgcolor="rgba(0,0,0,0)",
                                      xaxis=(dict(showgrid=False)),
                                      yaxis=(dict(showgrid=False)))
    st.plotly_chart(fig_rev23_by_campaign, use_container_width=True)

Q3,Q4 = st.columns(2)

with Q3:
    df4 = df_oppty.groupby(by='SF_Opprtunity_Id').sum()[['Stage']].reset_index()
    fig_spend_by_gender = px.pie(df4,names='stage',values='SF_Opprtunity_Id',title='<b>Stage</b>')
    fig_spend_by_gender.update_layout(title = {'x':0.5}, plot_bgcolor = "rgba(0,0,0,0)")
    st.plotly_chart(fig_spend_by_gender,use_container_width=True)