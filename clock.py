import requests
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    URL = "https://get-crypto-alert.herokuapp.com/api/alerts/sync/"
    requests.get(URL)

sched.start()
