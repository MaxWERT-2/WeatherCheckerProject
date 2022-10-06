import typer
from weather import get_weather_for_city


URL_NAME = 'https://world-weather.ru/pogoda/russia/'


def main(city: str):
    print(get_weather_for_city(city, URL_NAME))


if __name__ == '__main__':
    typer.run(main)
