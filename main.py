import streamlit as st
import plotly.express as px

st.title('Weather Forecast for the Next Days')
city=st.text_input(label="Place:")
days=st.select_slider(label='Forecast Days',
                 options=[1,2,3,4,5],
                 help="Select the number of forecasted days")
option=st.selectbox(label='Select data to view',
     options=['Temperature','Sky'])
st.subheader(f"{option} for the next {days} days in {city}")

#fake data
def get_data(days):
    dates=['1999-09-18','1999-09-19','1999-09-20','1999-09-21']
    temperatures=[19,25,23,27]
    temperatures=[days*i for i in temperatures]
    return dates,temperatures

d, t = get_data(days)

# source form Ploty or Bokeh
figure=px.line(x=d, y=t, labels={'x':'Date','y':'Temperature (C)'})
st.plotly_chart(figure)
