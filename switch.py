import requests
import json
#from covid19_data import JHU

# Format: <Data Source>.<Location>.<Statistic>
# For example to get data from John Hopkins University, review the following example:
# JHU.China.deaths

#print("The number of COVID-19 recoveries in the US: " + str(JHU.US.recovered))
#print("The number of confirmed COVID-19 cases in Texas: " + str(JHU.Texas.confirmed))

def takeCommand():
    q = input("Enter your value: ")
    return q
      

def get_temperature(json_data):
    temp_in_celcius = json_data['main']['temp']
    return temp_in_celcius

def get_weather_type(json_data):
    weather_type = json_data['weather'][0]['description']
    return weather_type

def get_wind_speed(json_data):
    wind_speed = json_data['wind']['speed']
    return wind_speed



def get_weather_data(json_data, city):
    description_of_weather = json_data['weather'][0]['description']
    weather_type = get_weather_type(json_data)
    temperature = get_temperature(json_data)
    wind_speed = get_wind_speed(json_data)
    weather_details = ''
    return weather_details + ("The weather in {} is currently {} with a temperature of {} degrees and wind speeds reaching {} km/ph".format(city, weather_type, temperature, wind_speed))



if __name__ == "__main__":
    q = takeCommand().lower()
    while True:

        

        if 'weather' in q:
               api_address = 'https://api.openweathermap.org/data/2.5/weather?q=Sydney,au&appid=a10fd8a212e47edf8d946f26fb4cdef8&q='
               city = input("City Name : ")
               units_format = "&units=metric"
               appid='97205bc44ad722755e6615dd8fd4e61c'
               final_url = api_address + city + units_format+appid
               json_data = requests.get(final_url).json()
               weather_details = get_weather_data(json_data, city)
    # print formatted data
               print(weather_details)

        elif 'news' in q:

            url = ('https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=018d28bad6844700ab73069a07c92fbe')

            response = requests.get(url)
            text = response.text
            my_json = json.loads(text)
            for i in range(0, 11):
                print(my_json['articles'][i]['title']) 

        #elif 'covid ' in q:
            #print("The number of COVID-19 recoveries in the US: " + str(JHU.INDIA.recovered))
            #print("The number of confirmed COVID-19 cases in Texas: " + str(JHU.INDIA.confirmed))
            else :
                print("wrong input")