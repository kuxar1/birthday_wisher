import datetime as dt
import smtplib
import pandas
import random

now = dt.datetime.now()
day = now.day
month = now.month

MY_EMAIL = 'mail@gmail.com'
PASSWORD = 'passwor'

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict('records')

letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
random_letter = random.choice(letter_list)

for i in range(len(data_dict)):
    if data_dict[i]["month"] == month and data_dict[i]["day"]:
        name = data_dict[i]["name"]
        with open(f"letter_templates/{random_letter}") as file:
            letter = file.read()
            letter = letter.replace("[NAME]", name)

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs='mail@gmail.com',
        msg=f'Subject:Happy Birthday \n\n {letter}'
    )
