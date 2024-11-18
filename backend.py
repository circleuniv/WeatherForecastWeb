import requests
import streamlit

WEATHER_API_KEY= streamlit.secrets['WEATHER_API_KEY']
#os.environ.get('WEATHER_API_KEY')

def get_date(City,forecast_days=None,kind=None):
    url=f"https://api.openweathermap.org/data/2.5/forecast?q={City}&appid={WEATHER_API_KEY}"
    data=requests.get(url)
    content=data.json()
    filter_data=content['list']
    nr_values=8*forecast_days
    filter_data=filter_data[:nr_values]
    dates=[templist['dt_txt'] for templist in filter_data]

    if kind == 'Temperature':
        filter_data=[templist['main']['temp']/10 for templist in filter_data]
    if kind == 'Sky':
        filter_data=[templist['weather'][0]['main'] for templist in filter_data]

    return dates,filter_data

if __name__ == '__main__':
    print(get_date('Taipei',forecast_days=3,kind='Temperature'))
