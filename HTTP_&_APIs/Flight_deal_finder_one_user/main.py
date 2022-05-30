# This file will need to use the DataManager,FlightSearch,
# FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
import smtplib
data_manager = DataManager()

sheet_data = data_manager.get_destination_data()
print(f"this is sh{sheet_data}")


flight_search = FlightSearch()


my_yahoo_email = "alsultan_adel1992@yahoo.com"
password_ = "cuzzgjblrbsficld"


ORIGIN_CITY_IATA = "RUH"
# CHECK FOR THE FIRST COLUMN IF "" THEN PRINT TESTING IN ALL OF THEM
if sheet_data[0]["IATA Code"] == "":
    from flight_search import FlightSearch

    flight_search = FlightSearch()
    for row in sheet_data:
        row["IATA Code"] = flight_search.get_destination_code(row["City"])
        data_manager.destination = sheet_data
        data_manager.update_destination_code()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flight(
        ORIGIN_CITY_IATA,
        destination["IATA Code"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    # if flight is not None and flight.price < destination["Lowest Price"]:
    #
    #     with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
    #         connection.starttls()  # to secure the connection
    #         connection.login(user=my_yahoo_email, password=password_)
    #         connection.sendmail(from_addr=my_yahoo_email, to_addrs="maax.1992@gmail.com",
    #                             msg=f"Subject:flight alert\n\n"
    #                                 f"Low price! only SAR{flight.price} to Fly from{flight.origin_city} to {flight.destination_city}"
    #                                 f" from {flight.out_date} to {flight.return_date} ")




