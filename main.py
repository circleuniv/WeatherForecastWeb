import streamlit as st
from streamlit import subheader

st.title('Weather Forecast for the Next Days')
city=st.text_input(label="Place:")
days=st.select_slider(label='Forecast Days',
                 options=[1,2,3,4,5],
                 help="Select the number of forecasted days")
option=st.selectbox(label='Select data to view',
     options=['Temperature','Sky'])

st.subheader(f"{option} for the next {days} days in {city}")

