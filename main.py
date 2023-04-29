import smtplib
from s_data import *

email = my_email
password = my_password

with smtplib.SMTP("smtp.gmail.com") as connection: #Standard Mail Transfer Protocol
    #Transport Layer Security
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(
        from_addr=email,
        to_addrs=to_sender,
        msg="Subject:App Test\n\nHELLO WORLD FROM AN EMAIL PYTHON APP"
        )
    # connection.close() #Unnecessary if used with the "with - as..."