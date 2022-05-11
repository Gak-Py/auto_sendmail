import smtplib
import datetime as dt
import pandas as pd
import random

import os
from os.path import join, dirname
from dotenv import load_dotenv

now = dt.datetime.now()

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
password = os.environ.get("PASSWORD") # 環境変数の値
my_email = os.environ.get("MY_EMAIL")

data = pd.read_csv("birthdays.csv")
data_dic = data.to_dict(orient="records")

for i in range(len(data_dic)):
    if now.month == data_dic[i]["month"] and now.day == data_dic[i]["day"]:
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as mail_temp:
            letter = mail_temp.read().replace("[NAME]", data_dic[i]["name"])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=data_dic[i]["email"],
                msg=f"Subject:Happy Birthday!\n\n{letter}")
    else:
        print("Not birthday")