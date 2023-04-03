import requests
import time


def get_price_XRPUSDT():
    headers = {'X-MBX-APIKEY': 'YOU KEY_API_BINANCE'}
    url = 'https://api.binance.com/api/v3/ticker/price?symbol=XRPUSDT'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        price = data['price']
        return price
    else:
        print('Ошибка при получении цены:', response.text)


def get_maxpriceonhour_XRPUSDT():
    interval = '1h'
    end_time = int(time.time() * 1000)
    start_time = end_time - (60 * 60 * 1000)
    url = f'https://api.binance.com/api/v3/klines?symbol=XRPUSDT&interval={interval}&startTime={start_time}&endTime={end_time}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        highest_value = max([candle[2] for candle in data])
        return highest_value
    else:
        print('Ошибка при получении максимального значения:', response.text)


def main():
    while True:
        price_XRPUSDT = float(get_price_XRPUSDT())
        maxpriceonhour_XRPUSDT = float(get_maxpriceonhour_XRPUSDT())
        if price_XRPUSDT < maxpriceonhour_XRPUSDT * 0.99:
            print('Цена упала на 1% или более! Закупайтейсь!')
        # else:
            # print(f'Цена: {price_XRPUSDT}, макимальная цена за час: {maxpriceonhour_XRPUSDT}')


if __name__ == "__main__":
    main()