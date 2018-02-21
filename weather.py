#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from myUtility import get_logger
from myUtility import get_soup_from_url
from myUtility import win10_notifier


def get_weather_info(url):
    try:
        file_logger = get_logger('weatherLog.txt')
        soup = get_soup_from_url(url)
        weather_result = str()
        temp_high = str()
        for weath_every in soup.find_all('li', class_='sky'):
            date = weath_every.h1.get_text()
            weath = weath_every.p.get_text()
            temperature_all = weath_every.find_all('p', class_='tem')
            if temperature_all[0].span:
                temp_high = temperature_all[0].span.get_text()
                temp_high += '~'
            temp_low = temperature_all[0].i.get_text()

            wind_all = weath_every.find_all('p', class_='win')
            wind = wind_all[0].i.get_text()
            weather_result += date + weath + '  ' + temp_high + temp_low + '  ' + wind + '\n'
            # logger.info("result: %s", weatherResult)


    except:
        file_logger.exception('catch exception!!!')
    print(weather_result)
    return weather_result


if __name__ == '__main__':
    weather_info = get_weather_info('http://www.weather.com.cn/weather/101020100.shtml')
    win10_notifier(weather_info, 60)
    logger = get_logger('weatherLog.txt')
    logger.info("\n%s", weather_info)
    sys.exit()
