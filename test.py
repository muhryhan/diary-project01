# first_name = 'Muhammad'
# last_name = 'Ryhan'
# # full_name = first_name + '' + last_name #jika tidk terlalu banyak var, maka baris ini digunakan
# full_name = f'{first_name} {last_name}' #jika terdpat banyak var, maka baris ini digunakan
# print(full_name)

# ====================================================================================================================

from datetime import datetime

today = datetime.now()

date_time = today.strftime('%Y-%M-%d-%H-%M-%S')

print(date_time)