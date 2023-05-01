# import smtplib
# from s_data import *

# email = my_email
# password = my_password

# with smtplib.SMTP("smtp.gmail.com") as connection: #Standard Mail Transfer Protocol
#     #Transport Layer Security
#     connection.starttls()
#     connection.login(user=email, password=password)
#     connection.sendmail(
#         from_addr=email,
#         to_addrs=to_sender,
#         msg="Subject:App Test\n\nHELLO WORLD FROM AN EMAIL PYTHON APP"
#         )
#     # connection.close() #Unnecessary if used with the "with - as..."


import datetime as dt

now = dt.datetime.now()
year = now.year
if year == 2023:
    print("TWENTY 20 🌲")
month = now.month
weekday = now.weekday()
# print(type(now)) # prints a datetime class
print(weekday) #computers count from 0 so '1' would be te second day of the week

date_of_birth = dt.datetime(year=1111, month=1, day=1, hour=4)
print(date_of_birth)