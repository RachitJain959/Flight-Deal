# This class is responsible for talking to the Flight Search API.

import requests
from flight_data import FlightData

TEQUILA_API_KEY = ""
TEQUILA_ENDPOINT = ""

search_header = {
    'apikey': TEQUILA_API_KEY,
}


class FlightSearch:

    def get_iata_code(self, city_name):
        search_parameters = {
            'term': city_name,
            'location_types': 'city',
        }
        response = requests.get(url=f'{TEQUILA_ENDPOINT}/locations/query', params=search_parameters,
                                headers=search_header).json()
        iata_code = response['locations'][0]['code']
        return iata_code

    def check_flight(self, date_from, date_to, currency, origin_city, destination):
        search_parameters = {
            'fly_from': origin_city,
            'fly_to': destination['iataCode'],
            'date_from': date_from,
            'date_to': date_to,
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'curr': currency,
            'flight_type': 'round',
        }
        search_response = requests.get(url=f'{TEQUILA_ENDPOINT}/v2/search', headers=search_header,
                                       params=search_parameters)
        # print(search_response.json())
        try:
            data = search_response.json()['data'][0]
        except IndexError:
            return None
        else:
            flight_data = FlightData(
                price=data['price'],
                city_from=data['cityFrom'],
                city_to=data['cityTo'],
                airport_from=data['flyFrom'],
                airport_to=data['flyTo'],
                flight_number=data['route'][0]['flight_no'],
                utc_departure=data['route'][0]['utc_departure'],
                utc_arrival=data['route'][0]['utc_arrival'],
            )
            # print(f'{flight_data.city_to}: {flight_data.price}')
            return flight_data
