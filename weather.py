#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import logging

import sys
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

# log
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler('weatherLog.txt', 'a', encoding='utf-8')
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter('%(asctime)s   %(message)s'))
logger.addHandler(handler)

try:
    weather_request = requests.get(
        'http://www.weather.com.cn/weather/101020100.shtml')
    weather_request.encoding = 'utf-8'

    soup = BeautifulSoup(weather_request.text, 'html.parser')
    weatherResult = str()
    tempHigh = str()
    for weathEvery in soup.find_all('li', class_='sky'):
        date = weathEvery.h1.get_text()
        weath = weathEvery.p.get_text()
        temperatureAll = weathEvery.find_all('p', class_='tem')
        if temperatureAll[0].span:
            tempHigh = temperatureAll[0].span.get_text()
            tempHigh += '~'
        tempLow = temperatureAll[0].i.get_text()

        windAll = weathEvery.find_all('p', class_='win')
        wind = windAll[0].i.get_text()
        weatherResult += date + weath + '  ' + tempHigh + tempLow + '  ' + wind + '\n'
        # logger.info("result: %s", weatherResult)

    logger.info("\n%s", weatherResult)
    toaster = ToastNotifier()
    toaster.show_toast('天气提醒', weatherResult, icon_path=None, duration=60, threaded=True)
except:
    logger.exception('catch exception!!!')

sys.exit()


