from s_data import *
import smtplib
import datetime as dt
import random

email = my_email
password = my_password

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes) 

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=to_sender,
            msg=f"Subject:Monday Motivation\n\n{quote}"
            )
