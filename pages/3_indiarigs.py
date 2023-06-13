import streamlit as st
import time
from PIL import Image
import base64
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
from annotated_text import annotated_text
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
#del st.session_state['date_value']
#for key in st.session_state.keys():
#    del st.session_state[key]

col1,col2 = st.columns([5,1])
shelf_logo = "https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/shelf drilling logo.png?raw=true"

with col1:
    st.header("RIGS JACKED UP IN INDIA REGION")
    st.write("SELECTED DATE - "+selected_date)
with col2:
    st.image(shelf_logo)
    home = st.button("HOME")
    if home:
        for key in st.session_state.keys():
            del st.session_state[key]
        switch_page("test")
with st.container():
    #col1,col2,col3,col4,col5,col6,col7,col8,col9,col10 = st.columns(10)
    
    #with col1:
    col1,col2,col3,col4,col5 = st.columns(5)
    
    with col1:
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='RTP']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        if south_east_asia_write == "RED":
            name_color = "#faa"
        elif south_east_asia_write == "YELLOW":
            name_color = "#fea"
        elif south_east_asia_write == "WHITE":
            name_color = "#afa"     
        else:
            name_color = "#FFF"
        annotated_text(("RON TAPPMEYER","",name_color))
        st.image("https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/india/RTP-MKT.jpg?raw=true")
        s1 = st.button("SUMMARY",key='1')
        
        if s1:
            #del st.session_state['date_value']
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "RTP"
            if 'color_value' not in st.session_state:
                st.session_state['color_value'] = south_east_asia_write
            switch_page('summary')
            
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='PSW']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        if south_east_asia_write == "RED":
            name_color = "#faa"
        elif south_east_asia_write == "YELLOW":
            name_color = "#fea"
        elif south_east_asia_write == "WHITE":
            name_color = "#afa"     
        else:
            name_color = "#FFF"
        annotated_text(("PARAMESHWARA","",name_color))
        st.image("https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/india/Shelf-Drilling-parameshwara.jpg?raw=true")
        s12 = st.button("SUMMARY",key='12')
        if s12:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "PSW"
            if 'color_value' not in st.session_state:
                st.session_state['color_value'] = south_east_asia_write
            switch_page('summary')
    with col2:
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='CET']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        if south_east_asia_write == "RED":
            name_color = "#faa"
        elif south_east_asia_write == "YELLOW":
            name_color = "#fea"
        elif south_east_asia_write == "WHITE":
            name_color = "#afa"     
        else:
            name_color = "#FFF"
        annotated_text(("THORNTON","",name_color))
        st.image("https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/india/Shelf-Drilling_CE-Thornton-.jpg?raw=true")
        s2 = st.button("SUMMARY",key='2')
        if s2:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "CET"
            if 'color_value' not in st.session_state:
                st.session_state['color_value'] = south_east_asia_write
            switch_page('summary')   
        
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='JTA']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        if south_east_asia_write == "RED":
            name_color = "#faa"
        elif south_east_asia_write == "YELLOW":
            name_color = "#fea"
        elif south_east_asia_write == "WHITE":
            name_color = "#afa"     
        else:
            name_color = "#FFF"
        annotated_text(("J T ANGEL","",name_color))
        st.image("https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/india/SJ-jackup-J-T-Angel.jpg?raw=true")
        s22 = st.button("SUMMARY",key='22')
        if s22:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "JTA"
            if 'color_value' not in st.session_state:
                st.session_state['color_value'] = south_east_asia_write
            switch_page('summary')
    with col3:
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='FGM']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        if south_east_asia_write == "RED":
            name_color = "#faa"
        elif south_east_asia_write == "YELLOW":
            name_color = "#fea"
        elif south_east_asia_write == "WHITE":
            name_color = "#afa"     
        else:
            name_color = "#FFF"
        annotated_text(("FG-MCCLINTOCK","",name_color))
        st.image("https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/india/Shelf-Drilling_FG-McClintock-..jpg?raw=true")
        
        s3 = st.button("SUMMARY",key='3')
        if s3:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "FGM"
            if 'color_value' not in st.session_state:
                st.session_state['color_value'] = south_east_asia_write
            switch_page('summary')
                
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='T02']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        if south_east_asia_write == "RED":
            name_color = "#faa"
        elif south_east_asia_write == "YELLOW":
            name_color = "#fea"
        elif south_east_asia_write == "WHITE":
            name_color = "#afa"     
        else:
            name_color = "#FFF"
        annotated_text(("TRIDENT-II","",name_color))
        st.image("https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/india/Trident-II_.jpg?raw=true")
        s32 = st.button("SUMMARY",key='32')
        if s32:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "T02"
            if 'color_value' not in st.session_state:
                st.session_state['color_value'] = south_east_asia_write
            switch_page('summary')
    with col4:
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='T12']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        if south_east_asia_write == "RED":
            name_color = "#faa"
        elif south_east_asia_write == "YELLOW":
            name_color = "#fea"
        elif south_east_asia_write == "WHITE":
            name_color = "#afa"     
        else:
            name_color = "#FFF"
        annotated_text(("TRIDENT-XII","",name_color))
        st.image("https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/india/Shelf-Drilling_Trident-XII_.jpg?raw=true")
                       
        s4 = st.button("SUMMARY",key='4')
        if s4:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "T12"
            if 'color_value' not in st.session_state:
                st.session_state['color_value'] = south_east_asia_write
            switch_page('summary')
        #st.button("SUMMARY   ")
    with col5:
        df_3_temp = df_2
        df_3_temp = df_3_temp[df_3_temp['date']==selected_date]
        df_3_temp = df_3_temp[df_3_temp['rig_no']=='KSN']
        south_east_asia_write = str(df_3_temp['color'].values).replace("['","").replace("']","")
        if south_east_asia_write == "RED":
            name_color = "#faa"
        elif south_east_asia_write == "YELLOW":
            name_color = "#fea"
        elif south_east_asia_write == "WHITE":
            name_color = "#afa"     
        else:
            name_color = "#FFF"
        annotated_text(("KEY SINGAPORE","",name_color))
        st.image("https://github.com/DEPTHJOURNEY/Automated-Offset-well-analysis/blob/main/rig_icon/india/Shelf-Drilling-key singapore.jpg?raw=true")
        s5 = st.button("SUMMARY",key='5')
        if s5:
            if 'rig_value' not in st.session_state:
                st.session_state['rig_value'] = "KSN"
            if 'color_value' not in st.session_state:
                st.session_state['color_value'] = south_east_asia_write
            switch_page('summary')
        #st.button("SUMMARY    ")
