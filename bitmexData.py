import requests


class Hourly():

    def __init__(self, startTime, endTime, symbol):
        self.startTime = startTime
        self.endTime = endTime
        self.binSize = '1h'
        self.count = '750'
        self.symbol = symbol

    def get_data(self, number):
        headers = {
                'Accept': 'application/json',
        }
        params = (
            ('binSize', self.binSize),
            ('partial', 'false'),
            ('symbol', self.symbol),
            ('count', '750'),
            ('start', str(number)),
            ('reverse', 'false'),
            ('startTime', self.startTime),
            ('endTime', self.endTime),
        )
        response = requests.get('https://www.bitmex.com/api/v1/trade/bucketed', headers=headers, params=params)

        return response.json()

    def get_data_all(self):
        data = []
        i = 0
        call = self.get_data(i)
        while len(call) != 0:
            print('Data loading...')
            data += call
            i += int(self.count)
            call = self.get_data(i)
        print('Data loaded.')

        return data


