from sheet import all_data,sheet
import gspread
from oauth2client.service_account import ServiceAccountCredentials



# This class is responsible for talking to the Google Sheet.

class DataManager:
    def __init__(self):
        self.destination = {}

    def get_destination_data(self):
        self.destination = all_data
        return self.destination

    def update_destination_code(self):

        new_data_list = []

        # each city is dictionary with all the information on the sheet
        # {'City': 'Paris', 'IATA Code': 'PAR', 'Lowest Price': 500}
        for city in self.destination:
            #print(city)

            new_data = city["IATA Code"]

            new_data_list.append(new_data)
        cell_list = sheet.range("B2:B10")
        cell_value = new_data_list
        for i, val in enumerate(cell_value):
            cell_list[i].value = val
        sheet.update_cells(cell_list)

