from bs4 import BeautifulSoup
import csv
import requests


def get_html(url):
    rr = requests.get(url)
    return rr.text


def write_csv(data):
    with open("irk_weather.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow((data["data"], data["temp_day"], data["temp_night"]))


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    d1 = soup.find("div", class_="b-weather-city-days-container-overflow")
    data_weather = d1.find_all("div", class_="day g-margin-bottom-10")
    temperature_day = d1.find_all("div", class_="g-font-size-21 g-margin-bottom-10")
    temperature_night = d1.find_all("div", class_="night g-font-size-17 g-color-gray g-margin-bottom-10")

    for i in range(len(data_weather)):
        data = data_weather[i].find("span").text
        temp_day = str(temperature_day[i])
        temp_night = str(temperature_night[i])
        print(data)
        print((temp_day[temp_day.find("\n") + 1::].partition("\n")[0]).strip())
        print((temp_night[temp_night.find("\n") + 1::].partition("\n")[0].strip()))
        info = {"data": data, "temp_day": (temp_day[temp_day.find("\n") + 1::].partition("\n")[0]).strip(),
                "temp_night": (temp_night[temp_night.find("\n") + 1::].partition("\n")[0].strip())}
        write_csv(info)


def main():
    url = "https://www.irk.ru/weather/"
    get_data(get_html(url))


if __name__ == "__main__":
    main()
