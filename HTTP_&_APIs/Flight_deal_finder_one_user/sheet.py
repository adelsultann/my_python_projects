import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets"
    , "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)

client = gspread.authorize(creds)
sheet = client.open("flight deals").sheet1

all_data = sheet.get_all_records()


# header = ['col1', 'col3']
# test_data = [{'col1': '1A', 'col3': '2A'}, {'col1': '1B', 'col3': '2B'}]
#
# wk.add_rows(len(test_data))
# cell_range = sheet.range("A2:B3")
# flattened_test_data = []
# for row in test_data:
#     for column in header:
#         flattened_test_data.append(row[column])
#
# for i, cell in enumerate(cell_range):
#     cell.value = flattened_test_data[i]
# wk.update_cells(cell_range)
#
