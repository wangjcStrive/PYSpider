#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import logging

import sys
from bs4 import BeautifulSoup
from win10toast import ToastNotifier


# log
# logger = logging.getLogger(__name__)
# logger.setLevel(level=logging.INFO)
# handler = logging.FileHandler('weatherLog.txt', 'a', encoding='utf-8')
# handler.setLevel(logging.INFO)
# handler.setFormatter(logging.Formatter('%(asctime)s   %(message)s'))
# logger.addHandler(handler)

def get_logger(file_name):
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    handler = logging.FileHandler(file_name, 'a', encoding='utf-8')
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter('%(asctime)s   %(message)s'))
    logger.addHandler(handler)
    return logger


def get_soup_from_url(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    return BeautifulSoup(res.text, 'html.parser')


def win10_notifier(weather_info, notify_duration=30):
    toaster = ToastNotifier()
    toaster.show_toast('天气提醒', weather_info, icon_path=None, duration=notify_duration, threaded=True)


def get_weather_info(url):
    try:
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
        logger.exception('catch exception!!!')
    return weather_result


if __name__ == '__main__':
    weather_info = get_weather_info('http://www.weather.com.cn/weather/101020100.shtml')
    win10_notifier(weather_info, 60)
    logger = get_logger('weatherLog.txt')
    logger.info("\n%s", weather_info)

