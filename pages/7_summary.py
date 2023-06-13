# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 16:50:36 2023

@author: Jayaraj
"""

import streamlit as st
import time
from PIL import Image
import base64
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
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
selected_color = st.session_state['color_value']

col1,col2,col3,col4 = st.columns([6,1,1,1])
shelf_logo = "https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/shelf drilling logo.png?raw=true"
with col1:
    st.title("SUMMARY")
    
with col4:
    st.image(shelf_logo)
with col3:
    home_button = st.button("HOME")
    if home_button:
        for key in st.session_state.keys():
            del st.session_state[key]
        switch_page("test")
with col2:
    change_data = st.button("MASTER-DATA")
    if change_data:
        switch_page("mainsheet")

if selected_color != "WHITE":
    col1,col2 = st.columns(2)
    with col1:
        st.write("----------------------")
    with col2:
        st.write("----------------------")
    df_sum = df_1
    df_sum = df_sum[df_sum['date']==selected_date ]
    df_sum = df_sum[df_sum['rig_no']==selected_rig]
    df_sum = df_sum[df_sum['color']==selected_color]
    df_show_sum = pd.DataFrame()
    df_show_sum['Time_count'] = df_sum['Time_count']
    df_show_sum['IADC_DESC'] = df_sum['IADC_DESC']
    df_show_sum['activity'] = df_sum['activity']
    df_show_sum['Time_count'] = df_show_sum['Time_count'].astype(float)
    df_show_sum['Time_count'].round(decimals=1)
    hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """
    
    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    st.table(df_show_sum)

    col1,col2 = st.columns(2)
    with col1:
        st.write("----------------------")
    with col2:
        st.write("----------------------")
        
st.header("DETAILED-ACTIVITY")
df_temp = df_1
df_temp = df_temp[df_temp['date']==selected_date ]
df_temp = df_temp[df_temp['rig_no']==selected_rig]
df_show = pd.DataFrame()
df_show['Time_count'] = df_temp['Time_count']
df_show['IADC_DESC'] = df_temp['IADC_DESC']
df_show['activity'] = df_temp['activity']
df_show['Time_count'] = df_show['Time_count'].round(decimals=1)
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)
st.table(df_show)
