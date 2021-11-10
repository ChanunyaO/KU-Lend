import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')
import django
django.setup()
from apscheduler.schedulers.blocking import BlockingScheduler
from ku_lend.function.reminder import send_reminder
from ku_lend.function.bill import send_bill

sched = BlockingScheduler()

@sched.scheduled_job('interval', hour=24)
def timed_call_send_mail():
    send_reminder()
    send_bill()

timed_call_send_mail()
sched.start()