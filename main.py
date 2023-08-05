from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

today = datetime.now()
date_from = today.strftime("%d/%m/%Y")
date_to = (today + timedelta(days=6*30)).strftime("%d/%m/%Y")

CURRENCY = 'GBP'
ORIGIN_CITY_IATA = 'LON'

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

for row in sheet_data:
    if row['iataCode'] == '':
        from flight_search import FlightSearch
        flight_search = FlightSearch()
        iata_code = flight_search.get_iata_code(row['city'])
        data_manager.put_destination_data(iata_code=iata_code, row_id=row['id'])

    flight_search = FlightSearch()
    flight_data = flight_search.check_flight(
        date_from=date_from,
        date_to=date_to, currency=CURRENCY,
        origin_city=ORIGIN_CITY_IATA,
        destination=row
    )

    if flight_data is None:
        continue

    if flight_data.price < row['lowestPrice']:
        notification_manager = NotificationManager(flight_data)
        notification_manager.send_mail()
