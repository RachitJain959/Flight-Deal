#    This class is responsible for structuring the flight data.

class FlightData:
    def __init__(self, price, city_from, city_to, airport_from, airport_to, flight_number, utc_departure, utc_arrival):
        self.city_from = city_from
        self.city_to = city_to
        self.airport_from = airport_from
        self.airport_to = airport_to
        self.price = price
        self.flight_number = flight_number
        self.departure = utc_departure
        self.arrival = utc_arrival
