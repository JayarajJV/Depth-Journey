import streamlit as st
import time
from PIL import Image
import base64
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import plotly.express as px
import pandas as pd
import numpy as np
import re
from datetime import datetime
import plotly.graph_objects as go

st.set_page_config(layout='wide',initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
path_1 = "https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/IADC_WELL_RPT_test.xlsx?raw=true"
path_2 = "https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/IADC_WELL_RPT_rig_color.xlsx?raw=true"
path_3 = "https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/IADC_WELL_RPT_reg_color.xlsx?raw=true"
df_1 =  pd.read_excel(path_1)
df_2 =  pd.read_excel(path_2)
df_3 =  pd.read_excel(path_3)


selected_date = st.session_state['date_value']
selected_rig = st.session_state['rig_value']
df_1['date']= pd.to_datetime(df_1['date']).dt.date
df_1  = df_1.sort_values(by='date',ascending=False)

col1,col2 = st.columns([5,1])
shelf_logo = "https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/shelf drilling logo.png?raw=true"
with col1:
    st.header("MASTERSHEET")
with col2:
    home_button = st.button("HOME")
    if home_button:
        for key in st.session_state.keys():
            del st.session_state[key]
        switch_page("test")
    st.image(shelf_logo)










col1,col2,col3,col4,col5,col6,col7,col8 = st.columns([3,3,3,3,3,3,2,2])
with col1:
    df_temp = df_1
    reg = st.selectbox("REGION",df_temp['region_name'].unique())
    df_temp = df_temp[df_temp['region_name'] == reg]
with col2:
    rig = st.selectbox("RIG",df_temp['rig_name'].unique())
    df_temp = df_temp[df_temp['rig_name'] == rig]
with col3:
    well = st.selectbox("WELL NO",df_temp['well_name'].unique())
    df_temp = df_temp[df_temp['well_name'] == well]
    df_prob = df_temp
with col7:
    prob = st.selectbox("PROBLEMS",df_temp['color'].unique())
    df_prob = df_prob[df_prob['color'] == prob]
with col4:
    date = st.selectbox("DATE",df_temp['date'].unique())
    
with col5:
    month = st.selectbox("MONTH",df_temp['month_wise'].unique())
with col6:
    date_b = st.button("DATE")
    
    month_b = st.button("MONTH")
    
col1,col2 = st.columns(2)
with col1:
    st.write("----------------------")
with col2:
    st.write("----------------------")

hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
st.markdown(hide_table_row_index, unsafe_allow_html=True)
t1,t2 = st.columns(2)
col1,col2,col3,col4 =st.columns([3.5,3.5,3.5,2])
if date_b:
    
    df_show = pd.DataFrame()
    df_show['date']  = df_temp['date']
    df_show=df_show[df_show['date']==date]
    df_show['ACTIVITY'] = df_temp['activity']
    df_show['IADC_DESC'] = df_temp['IADC_DESC']
    df_show['Time'] = df_temp['Time_count']
    st.table(df_show)
    
    df_rig_no=df_show.dropna(subset=['Time'])
    elapsedtime = pd.DataFrame()
    elapsedtime['IADC_DESC'] = df_rig_no['IADC_DESC']
    elapsedtime['Time_count'] = df_rig_no['Time']
    elapsedtime = elapsedtime.groupby(by=elapsedtime['IADC_DESC']).sum()
    #elapsedtime = df_graph.groupby(by=df_graph['code']).sum()
    #ax.pie(elapsedtime['ELAPSED_TIME'],labels = elapsedtime.index)
    #ax.legend(title='OPERATIONAL TIME DISTRIBUTION')
    fig_rig = go.Figure(
        go.Pie(
        labels = elapsedtime.index,
        values =elapsedtime['Time_count'],
        hoverinfo = "label+percent",
        textinfo = "value"
    ))
    with t1:
        st.write("OPERATION DISTRIBUTION (FOR SELECTED REGION-RIG-WELL)")
        st.plotly_chart(fig_rig)
    
    df_temp_prob = df_prob[df_prob['date']==date]
    df_rig_no=df_temp_prob.dropna(subset=['Time_count'])
    elapsedtime = pd.DataFrame()
    elapsedtime['IADC_DESC'] = df_rig_no['IADC_DESC']
    elapsedtime['Time_count'] = df_rig_no['Time_count']
    elapsedtime = elapsedtime.groupby(by=elapsedtime['IADC_DESC']).sum()
    #elapsedtime = df_graph.groupby(by=df_graph['code']).sum()
    #ax.pie(elapsedtime['ELAPSED_TIME'],labels = elapsedtime.index)
    #ax.legend(title='OPERATIONAL TIME DISTRIBUTION')
    fig_rig = go.Figure(
        go.Pie(
        labels = elapsedtime.index,
        values =elapsedtime['Time_count'],
        hoverinfo = "label+percent",
        textinfo = "value"
    ))
    with t2:
        st.write("OPERATION DISTRIBUTION (FOR SELECTED REGION-RIG-WELL-PROBLEM)")
        st.plotly_chart(fig_rig)
    
    
    
    
    df_show_reg = df_1[(df_1['region_name'] == reg) & (df_1['date'] == date)]
    df_rig_no=df_show_reg.dropna(subset=['Time_count'])
    elapsedtime = pd.DataFrame()
    elapsedtime['IADC_DESC'] = df_rig_no['IADC_DESC']
    elapsedtime['Time_count'] = df_rig_no['Time_count']
    elapsedtime = elapsedtime.groupby(by=elapsedtime['IADC_DESC']).sum()
    #elapsedtime = df_graph.groupby(by=df_graph['code']).sum()
    #ax.pie(elapsedtime['ELAPSED_TIME'],labels = elapsedtime.index)
    #ax.legend(title='OPERATIONAL TIME DISTRIBUTION')
    fig_rig = go.Figure(
        go.Pie(
        labels = elapsedtime.index,
        values =elapsedtime['Time_count'],
        hoverinfo = "label+percent",
        textinfo = "value"
    ))
    with col1:
        st.write("OPERATION DISTRIBUTION (REGION VS DAY)")
        st.plotly_chart(fig_rig)

    df_show_rig = df_1[(df_1['rig_name'] == rig) & (df_1['date'] == date)]
    df_rig_no=df_show_rig.dropna(subset=['Time_count'])
    elapsedtime = pd.DataFrame()
    elapsedtime['IADC_DESC'] = df_rig_no['IADC_DESC']
    elapsedtime['Time_count'] = df_rig_no['Time_count']
    elapsedtime = elapsedtime.groupby(by=elapsedtime['IADC_DESC']).sum()
    #elapsedtime = df_graph.groupby(by=df_graph['code']).sum()
    #ax.pie(elapsedtime['ELAPSED_TIME'],labels = elapsedtime.index)
    #ax.legend(title='OPERATIONAL TIME DISTRIBUTION')
    fig_rig = go.Figure(
        go.Pie(
        labels = elapsedtime.index,
        values =elapsedtime['Time_count'],
        hoverinfo = "label+percent",
        textinfo = "value"
    ))
    with col2:
        st.write("OPERATION DISTRIBUTION (RIG VS DAY)")
        st.plotly_chart(fig_rig)

    df_show_rig = df_1[(df_1['well_name'] == well) & (df_1['date'] == date)]
    df_rig_no=df_show_rig.dropna(subset=['Time_count'])
    elapsedtime = pd.DataFrame()
    elapsedtime['IADC_DESC'] = df_rig_no['IADC_DESC']
    elapsedtime['Time_count'] = df_rig_no['Time_count']
    elapsedtime = elapsedtime.groupby(by=elapsedtime['IADC_DESC']).sum()
    #elapsedtime = df_graph.groupby(by=df_graph['code']).sum()
    #ax.pie(elapsedtime['ELAPSED_TIME'],labels = elapsedtime.index)
    #ax.legend(title='OPERATIONAL TIME DISTRIBUTION')
    fig_rig = go.Figure(
        go.Pie(
        labels = elapsedtime.index,
        values =elapsedtime['Time_count'],
        hoverinfo = "label+percent",
        textinfo = "value"
    ))
    with col3:
        st.write("OPERATION DISTRIBUTION (WELL VS DAY)")
        st.plotly_chart(fig_rig)




if month_b:    
    df_show = pd.DataFrame()
    df_show['date']  = df_temp['date']
    df_show['month_wise']  = df_temp['month_wise']
    df_show=df_show[df_show['month_wise']==month]
    df_show['ACTIVITY'] = df_temp['activity']
    df_show['IADC_DESC'] = df_temp['IADC_DESC']
    df_show['Time'] = df_temp['Time_count']
    st.table(df_show)

    df_rig_no=df_show.dropna(subset=['Time'])
    elapsedtime = pd.DataFrame()
    elapsedtime['IADC_DESC'] = df_rig_no['IADC_DESC']
    elapsedtime['Time_count'] = df_rig_no['Time']
    elapsedtime = elapsedtime.groupby(by=elapsedtime['IADC_DESC']).sum()
    #elapsedtime = df_graph.groupby(by=df_graph['code']).sum()
    #ax.pie(elapsedtime['ELAPSED_TIME'],labels = elapsedtime.index)
    #ax.legend(title='OPERATIONAL TIME DISTRIBUTION')
    fig_rig = go.Figure(
        go.Pie(
        labels = elapsedtime.index,
        values =elapsedtime['Time_count'],
        hoverinfo = "label+percent",
        textinfo = "value"
    ))
    with t1:
        st.write("OPERATION DISTRIBUTION (FOR SELECTED REGION-RIG-WELL)")
        st.plotly_chart(fig_rig)
    
    df_temp_prob = df_prob[df_prob['month_wise']==month]
    df_rig_no=df_temp_prob.dropna(subset=['Time_count'])
    elapsedtime = pd.DataFrame()
    elapsedtime['IADC_DESC'] = df_rig_no['IADC_DESC']
    elapsedtime['Time_count'] = df_rig_no['Time_count']
    elapsedtime = elapsedtime.groupby(by=elapsedtime['IADC_DESC']).sum()
    #elapsedtime = df_graph.groupby(by=df_graph['code']).sum()
    #ax.pie(elapsedtime['ELAPSED_TIME'],labels = elapsedtime.index)
    #ax.legend(title='OPERATIONAL TIME DISTRIBUTION')
    fig_rig = go.Figure(
        go.Pie(
        labels = elapsedtime.index,
        values =elapsedtime['Time_count'],
        hoverinfo = "label+percent",
        textinfo = "value"
    ))
    with t2:
        st.write("OPERATION DISTRIBUTION (FOR SELECTED REGION-RIG-WELL-PROBLEM)")
        st.plotly_chart(fig_rig)

    df_show_reg = df_1[(df_1['region_name'] == reg) & (df_1['month_wise'] == month)]
    df_rig_no=df_show_reg.dropna(subset=['Time_count'])
    elapsedtime = pd.DataFrame()
    elapsedtime['IADC_DESC'] = df_rig_no['IADC_DESC']
    elapsedtime['Time_count'] = df_rig_no['Time_count']
    elapsedtime = elapsedtime.groupby(by=elapsedtime['IADC_DESC']).sum()
    #elapsedtime = df_graph.groupby(by=df_graph['code']).sum()
    #ax.pie(elapsedtime['ELAPSED_TIME'],labels = elapsedtime.index)
    #ax.legend(title='OPERATIONAL TIME DISTRIBUTION')
    fig_rig = go.Figure(
        go.Pie(
        labels = elapsedtime.index,
        values =elapsedtime['Time_count'],
        hoverinfo = "label+percent",
        textinfo = "value"
    ))
    with col1:
        st.write("OPERATION DISTRIBUTION (REGION VS MONTH)")
        st.plotly_chart(fig_rig)

    df_show_rig = df_1[(df_1['rig_name'] == rig) & (df_1['month_wise'] == month)]
    df_rig_no=df_show_rig.dropna(subset=['Time_count'])
    elapsedtime = pd.DataFrame()
    elapsedtime['IADC_DESC'] = df_rig_no['IADC_DESC']
    elapsedtime['Time_count'] = df_rig_no['Time_count']
    elapsedtime = elapsedtime.groupby(by=elapsedtime['IADC_DESC']).sum()
    #elapsedtime = df_graph.groupby(by=df_graph['code']).sum()
    #ax.pie(elapsedtime['ELAPSED_TIME'],labels = elapsedtime.index)
    #ax.legend(title='OPERATIONAL TIME DISTRIBUTION')
    fig_rig = go.Figure(
        go.Pie(
        labels = elapsedtime.index,
        values =elapsedtime['Time_count'],
        hoverinfo = "label+percent",
        textinfo = "value"
    ))
    with col2:
        st.write("OPERATION DISTRIBUTION (RIG VS MONTH)")
        st.plotly_chart(fig_rig)

    df_show_rig = df_1[(df_1['well_name'] == well) & (df_1['month_wise'] == month)]
    df_rig_no=df_show_rig.dropna(subset=['Time_count'])
    elapsedtime = pd.DataFrame()
    elapsedtime['IADC_DESC'] = df_rig_no['IADC_DESC']
    elapsedtime['Time_count'] = df_rig_no['Time_count']
    elapsedtime = elapsedtime.groupby(by=elapsedtime['IADC_DESC']).sum()
    #elapsedtime = df_graph.groupby(by=df_graph['code']).sum()
    #ax.pie(elapsedtime['ELAPSED_TIME'],labels = elapsedtime.index)
    #ax.legend(title='OPERATIONAL TIME DISTRIBUTION')
    fig_rig = go.Figure(
        go.Pie(
        labels = elapsedtime.index,
        values =elapsedtime['Time_count'],
        hoverinfo = "label+percent",
        textinfo = "value"
    ))
    with col3:
        st.write("OPERATION DISTRIBUTION (WELL VS MONTH)")
        st.plotly_chart(fig_rig)
