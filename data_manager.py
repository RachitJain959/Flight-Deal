#    This class is responsible for talking to the Google Sheet.\

import requests

SHEETY_ENDPOINT_PRICES = ""
SHEETY_ENDPOINT_USERS = ""
sheety_header = {
    'Authorization': ''
}


class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.user_data = {}

    def get_user_data(self):
        response = requests.get(url=SHEETY_ENDPOINT_USERS, headers=sheety_header)
        self.user_data = response.json()['users']
        return self.user_data

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT_PRICES, headers=sheety_header)
        self.destination_data = response.json()['prices']
        return self.destination_data

    def put_destination_data(self, iata_code, row_id):
        new_data = {
            'price': {
                'iataCode': iata_code,
            },
        }
        response = requests.put(url=f'{SHEETY_ENDPOINT_PRICES}/{row_id}', json=new_data, headers=sheety_header)
        print(response.text)
