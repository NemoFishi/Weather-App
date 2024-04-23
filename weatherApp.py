# Name: Nikolis Ratjavong
# Date: 29 January 2024
# WeatherApp CL Project

import requests

api_key = "6feb38e8c25bdc85fb588e80f5015418"

website = "api.openweathermap.org/data/2.5/forecast?"

# user input Zipcode
zipcode = input("Enter zipcode : ")

# create complete url
complete_url = "http://" + website + "zip=" + zipcode + ",us&" + "appid=" + api_key

# get response from url
response = requests.get(complete_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Reformat Json into Pyton HTTP
    x = response.json()

    # print(x)

    # Check if the response is equal to 200 data
    if x["cod"] == "200":
        # store the value of "list" key in variable y
        y = x['list']

        for i in range(4, 24, 8):

            # Store dt_txt into area Date
            areaDate = y[i]['dt_txt']

            # store the 'temp' into curr_temp
            (curr_temp) = y[i]['main']['temp']
            curr_temp = (9 / 5) * (curr_temp - 273.15) + 32

            # store the 'temp_min' into low_temp
            low_temp = y[i - 4]['main']['temp_min']
            low_temp = (9 / 5) * (low_temp - 273.15) + 32

            # store the 'temp_max' into max_temp
            max_temp = y[i + 4]['main']['temp_max']
            max_temp = (9 / 5) * (max_temp - 273.15) + 32

            # store the weather value into variable z
            z = y[i]['weather']

            # check weather for corrisponding description
            weat_desc = z[0]["description"]

            # print
            print(" The zip code location is: " +
                  zipcode +
                  "\n The date is :" + areaDate +
                  "\n The Temperature is " +
                  str(round(curr_temp, 2)) + "°F" +
                  "\n with a high of " +
                  str(round(max_temp, 2)) + "°F" +
                  "\n and a low of " +
                  str(round(low_temp, 2)) + "°F" +
                  "\n with " +
                  str(weat_desc) +
                  "\n ")
    else:
        print("Invalid data in the response.")
else:
    print("Error in the API request. Status code:", response.status_code)

