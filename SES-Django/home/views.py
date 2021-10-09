from django.http import response
from home.models import Event
from django.contrib.auth import login
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from home import qrcode, sendMail,encryption_util
from .models import Attendees, Event
import json
from django.core import serializers

# Create your views here.
def index(request):
    return render(request,"index.html")

def home(request):
   
    if request.user.is_anonymous:
        return redirect("accounts/login")
    
    if request.method == "POST":
        userEmail=request.user.email
        title=request.POST["title"]
        date=request.POST["eventdate"]
        print(type(date))
        #date=date.strftime("%d%m%y")
        startTime=request.POST["starttime"]
        #startTime=startTime.strftime("%H%M%S")
        endTime=request.POST["endtime"]
        #endTime=endTime.strftime("%d%m%y%H%M%S")
        destination=request.POST["destination"]
        #is meeting
        is_event=False
        if request.POST["isevent"] == "True":
            is_event=True

        eventid=userEmail+date+startTime
        event=Event(uid=request.user,eid=eventid,event_name=title,date=date,start_time=startTime,end_time=endTime,is_event=is_event,destination=destination)
        event.save()
        print("added in db")
        if is_event==False:
            attendeesEmail=request.POST["attendeesemail"]
            attendeesEmailList=attendeesEmail.split(",")
            print(attendeesEmailList)
            eveid=userEmail+date+startTime
            for aemail in attendeesEmailList:
                s = eventid+aemail
                print("->>>>>>>>>>>>>",s)
                qrcodeStatus=qrcode.generate_qrcode(s)
                if qrcodeStatus==True:
                    sendMail.mailMeeting(aemail,s,eveid)
                attendee=Attendees(eid=eventid,attendees_email=aemail)
                attendee.save()
                print("attendee added in db")


        return redirect("/home")

        # for aemail in attendeesEmailList:
        #     print(userEmail,title,date,startTime,endTime,aemail)
        #     # String which represents the QR code
        #     s = userEmail+date+startTime+aemail
        #     print("->>>>>>>>>>>>>",s)
        #     qrcodeStatus=qrcode.generate_qrcode(s)
        #     if qrcodeStatus==True:
        #             sendMail.mail(aemail,s)


    eventslist=Event.objects.filter(uid = request.user)    
    mylist=[]
    for event in eventslist:
        if event.is_event:
            mylist.append({'eventdata':event,'url':"registerevent/"+encryption_util.encrypt(event.eid),"count":Attendees.objects.filter(eid=event.eid).count()})
        else:
            mylist.append({'eventdata':event,'url':" "})
    return render(request,"home.html",{"events":mylist})

def registerEvent(request,eid):
    params={}
    if request.method=="GET":
        print("eid= ",eid)
        decodedEid=encryption_util.decrypt(eid)    
        print("--------------->",decodedEid)
        event=Event.objects.get(eid=decodedEid)
        params={"events": event}

    if request.method=="POST":
        eveid=request.POST["eveid"]
        aname=request.POST["aname"]
        aemail=request.POST["aemail"]
        aage=request.POST["aage"]
        aphone=request.POST["aphone"]

        attendee=Attendees(eid=eveid,attendees_name=aname,attendees_email=aemail,attendees_phone=aphone,age=aage)
        attendee.save()
        print("attendee added in db")

        s = eveid+aemail
        print("->>>>>>>>>>>>>",s)
        qrcodeStatus=qrcode.generate_qrcode(s)
        if qrcodeStatus==True:
           sendMail.mailEvent(aemail,s,eveid)
 
        return redirect("/successfulsubmition",{"mail":aemail})
    return render(request,"registerevent.html",params)    

def successfulSubmit(request):

    return render(request,"successfulsubmition.html")


def downloadJson(request):
    if request.method=="POST":
        eid=request.POST["eventid"]
        data = Attendees.objects.filter(eid=eid)
        print(type(data))
        print(data)
        map = {}
        for i in data:
            map[eid+i.attendees_email] = {"name":i.attendees_name,"email":i.attendees_email,"phone":i.attendees_phone,"age":i.age}
        
        response = HttpResponse(json.dumps(map), content_type='application/json')
        response['Content-Disposition'] = 'attachment; data.json"'
    return response
