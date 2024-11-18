import streamlit as st
import plotly.express as px
import backend

# Add title, text input, slider, selectbox, and subheader
st.title('Weather Forecast for the Next Days')
city=st.text_input(label="Place:")
days=st.select_slider(label='Forecast Days',
                 options=[1,2,3,4,5],
                 help="Select the number of forecasted days")
option=st.selectbox(label='Select data to view',
     options=['Temperature','Sky'])
st.subheader(f"{option} for the next {days} days in {city}")

if city:
    try:
        #Get the temperature or sky data depends on option
        dates,data= backend.get_date(city,forecast_days=days,kind=option)

        if option == 'Temperature':
            # create a temperatuer plot
            figure=px.line(x=dates, y=data, labels={'x':'Date','y':'Temperature (C)'})
            st.plotly_chart(figure)
        if option =='Sky':
            images={'Clear':'images/clear.png',
                    'Clouds':'images/cloud.png',
                    'Rain':'images/rain.png',
                    'Snow':'images/snow.png'}
            skyMage=[images[condition] for condition in data]

            # show 5 images and dates per row
            columns_per_row=5
            for i in range(0,len(skyMage),columns_per_row):
                cols=st.columns(columns_per_row)
                for col,(img_url,date) in zip(cols,zip(skyMage[i:i+columns_per_row],dates[i:i+columns_per_row])):
                    col.image(img_url,use_container_width=True,caption=date)
           # st.image(skyMage,width=150)
    except KeyError:
        st.write('This place does not exist.')

