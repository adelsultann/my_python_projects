import requests
from datetime import timedelta,datetime



tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))


header = ['col1', 'col2']

#
# test_data = [{'col1': '1A', 'col2': '2A'}, {'col1': '1B', 'col2': '2B'}]
#
# for row in test_data:
#     print(f"this is row {row}")
#     for column in header:
#         print("____________________________")
#         print(header)
#
#
#
# for i in range(1,3):
#     for n in range(1,3):
#         print(i)
#         print(f"this is n {n}")


# 5 rows
for name in range(5):
    # 3 column
    for j in range(3):
        print('*', end='')
    print()