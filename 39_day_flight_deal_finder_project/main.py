# 4. Pass the data back to the main.py file, so that you can print the data from main.py
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "LON"
twilio_number = '+12055824835'
twilio_sid = 'ACa2267883c87357e3be233230b4844550'
twilio_auth = 'bfefce02d3a522558da536306af13541'

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight.price < destination['lowestPrice']:
        sms_body = f'Low price alert! only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}'
        sms_sender = NotificationManager(
            sid=twilio_sid,
            auth_token=twilio_auth,
            phone_num=twilio_number,
            sms_body=sms_body
        )
        sms_sender.send_sms()
