from application.worker import celery
from application.models import User,Post
from datetime import datetime
from jinja2 import Template
from celery.schedules import crontab
from httplib2 import Http
import json
from application.mail_sent import send_email,main
# from email import encoders
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import smtplib

@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, monthly_report_by_email.s() )
    # sender.add_periodic_task(crontab(hour=7, minute=30, day_of_week=1), monthly_report_by_email.s() )
    sender.add_periodic_task(10.0, daily_reminder_by_email.s())
    # sender.add_periodic_task(10.0, webhook_chat.s())
    # sender.add_periodic_task(crontab(hour=7, minute=30, day_of_week=1), daily_reminder_by_email.s())

    


@celery.task()
def print_current_time():
    print("start")
    now = datetime.now()
    print("now in task ", now)
    dtstr = now.strftime("%d/%m/%Y %H:%M:%S")
    # print("inside Task")
    # print("hello "+ name )
    print("complete")
    return dtstr
    

@celery.task()
def daily_reminder_by_email():
    all_users=User.query.all()
    for user in all_users:
        c = 0
        user_idd = user.user_id
        list_details = Post.query.filter_by(user_id=user_idd).all()
        # # card_details = Card.query.filter_by(
        # #     user_id=user_idd).all()
        # for card in card_details:
        #     if card.completed == 'Incomplete':
        #         c = c + 1

                # with open("mail.html", 'r') as h:
                #     temp=Template(h.read())
                #    send_email(user.email_id, subject="Daily Reminder",message=temp.render(name=user,lists = list_details,cards= card_details),)
        
        with open("mail.html", 'r') as h:
            temp=Template(h.read())
            send_email(user.email_id, subject="Daily Reminder",message=temp.render(name=user))
    


    return "khandelwal hu maii"
@celery.task()
def monthly_report_by_email():
    all_users=User.query.all()
    for user in all_users:
        user_idd = user.user_id
        list_details = Post.query.filter_by(user_id=user_idd).all()
        # card_details = Card.query.filter_by(
        #     user_id=user_idd).all()
        inc = 0
        com = 0
        # for i in card_details:
        #     if(i.completed == "Incomplete"):
        #         inc = inc + 1
        # com = len(card_details) - inc
        length = len(list_details)
        with open("progress.html", 'r') as h:
            temp=Template(h.read())
            send_email(user.email_id, subject="Monthly Report  ",message=temp.render(name=user,length = length,lists = list_details),)

    return "sarthak_hu_maii"

@celery.task()
def webhook_chat():

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()

    data = {'text': 'dont miss any update about the community keep yourself posted and keep posting '}

    res = http_obj.request('https://chat.googleapis.com/v1/spaces/AAAAfgrDsWs/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=IfztE-8BZPIo2MDqMYS7PUh3kOxEkBZ9JqAmFPjCPtw%3D', method='POST', headers=message_headers, body=json.dumps(data))

    print(res)