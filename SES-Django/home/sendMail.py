from home.models import Event
from django.core.mail import EmailMessage
import os

def mailEvent(to, fname, eveid):
   event=Event.objects.get(eid=eveid)
   mail = EmailMessage(
       'Your Registration for Event was Successful!!',
       '''Please Find the details below:
          Event Title: {}
          Date: {}
          Destination: {}
          Timings: {} to {}
       '''.format(event.event_name,event.date,event.destination,event.start_time,event.end_time),
       'noreply@smartentarancesystem.com',
       [to],
   )#    time.sleep(5)
   print("STARTING TO SEND MAIL--------------")
   mail.attach_file('media/qrcodes/{fname}.png'.format(fname=fname))
   mail.send()

   print("DONE ~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   os.remove('media/qrcodes/{fname}.png'.format(fname=fname))


def mailMeeting(to, fname, eveid):
   event=Event.objects.get(eid=eveid)
   mail = EmailMessage(
       'You Have Been Invited To The Meeting!!',
       '''Please Find the details below:
          Meeting Title: {}
          Date: {}
          Destination: {}
          Timings: {} to {}
       '''.format(event.event_name,event.date,event.destination,event.start_time,event.end_time),
       'noreply@smartentarancesystem.com',
       [to],
   )
#    time.sleep(5)
   print("STARTING TO SEND MAIL--------------")
   mail.attach_file('media/qrcodes/{fname}.png'.format(fname=fname))
   mail.send()

   print("DONE ~~~~~~~~~~~~~~~~~~~~~~~~~~~")
   os.remove('media/qrcodes/{fname}.png'.format(fname=fname))  