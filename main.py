from keep_alive import keep_alive
import schedule

import time

import requests

import pandas as pd

keep_alive()


data = pd.read_csv("qoutes-V3.csv")

token = "EAAbpjm1UCZBkBAEYKZBMqlWwg1LlErQFm7BXPw3R0JvSO3wUssC5ZCQ9ug0f7R05ntuEsa543ngNHoH13bT0ZCiUzJdjB2xg8OODqlxcgrt5kfSqAU3cQZCEndrd6zv6rpAXATQRvZCD1MsJnnkj1UkIrsBxrg2xnzXG8zyiFRoYSZCewlzJzc8E"

page_id = "106716052356455"
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

  
