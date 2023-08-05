# This class is responsible for sending notifications with the deal flight details.
from data_manager import DataManager
import smtplib
import os

data_manager = DataManager()
users = data_manager.get_user_data()

MY_EMAIL = os.environ.get('')
PASSWORD = os.environ.get('')


class NotificationManager:
    def __init__(self, flight_data):
        self.message = f"Low Price Alert! Only ${flight_data.price} to fly from {flight_data.city_from}-" \
                       f"{flight_data.airport_from} to {flight_data.city_to}-{flight_data.airport_to} from " \
                       f"{flight_data.departure} to {flight_data.arrival}"

    def send_mail(self):
        for user in users:
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=user['email'],
                    msg=f"Subject: Cheap FLight!\n\n\n{self.message}".encode('utf-8'),
                )
