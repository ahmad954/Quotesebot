from keep_alive import keep_alive
import schedule

import time

import requests

import pandas as pd

keep_alive()


data = pd.read_csv("qoutes-V3.csv")

token = "YOUR-FACEBOOK-TOKEN"

page_id = "YOUR-PAGE-ID"
url = f"https://graph.facebook.com/{page_id}/feed"


def job():
  msg = f'{data["AUTHOR"][0]}\n"{data["QUOTE"][0]}"'
  payload = {'message': msg, 'access_token': token}
  data.drop([0],inplace=True)
  data.reset_index(inplace=True,drop=True)
  req = requests.post(url, payload)
  print(req.text)


schedule.every().hour.at(":11").do(job)

while True:
  schedule.run_pending()
  time.sleep(1)

  
