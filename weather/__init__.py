import pickle
import time
import requests
from bs4 import BeautifulSoup


def cache(ttl=5 * 60):
    def decorator(func):
        def wrapper(*args, **kwargs):
            cur_time = time.time()
            cash_dict = {}
            result = ''
            flag = 1
            try:
                f = open('cash.pickle', 'rb')
                cash_dict = pickle.load(f)
                cash_list = cash_dict.copy().items()
                for i in cash_list:
                    if cur_time - i[1][0] >= ttl:
                        cash_dict.pop(i[0])
                    elif i[0][0] == args[0]:
                        result = i[1][1]
                        flag = 0
                if flag:
                    result = func(*args, **kwargs)
                f.close()
            except FileNotFoundError:
                result = func(*args, **kwargs)
            cash_dict.update({args: [cur_time, result]})
            if not flag:
                result = 'The result is taken from the cache\n' + result
            f = open('cash.pickle', 'wb')
            pickle.dump(cash_dict, f)
            return result

        return wrapper

    return decorator


@cache(ttl=5 * 60)
def get_weather_for_city(city: str, url: str):
    try:
        r = requests.get(url + city)
        soup = BeautifulSoup(r.text, 'lxml')
        s = soup.find(id="weather-now-number").get_text()
        return 'Current weather in ' + city + ': ' + s[:len(s) - 1]
    except BaseException:
        return 'There is no city with this name in Russia'
