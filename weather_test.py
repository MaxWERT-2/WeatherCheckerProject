from weather import get_weather_for_city


def simple_test():
    assert (1, 2, 3) == (1, 2, 3)


def cache_test():
    city = 'moscow'
    url = 'https://world-weather.ru/pogoda/russia/'
    assert 'The result is taken from the cache\n' + get_weather_for_city(city, url) == get_weather_for_city(city, url)
