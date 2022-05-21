# Smart Entrance System

## Introduction

Security is a major issue while arranging any function. Prevention of unauthorized person entering the function is necessary. So for this there is need of security guard at the entrance that checks whether the person is allowed or not. For that there is also a need of pass or a card that shows that the person is invited in the function. Smart Entrance System automates this task and provides better security. Smart Entrance System is made using various technologies like Arduino, Image Processing and Django.

## Overview

The event organizer creates the event and sends the URL of the form to the guests. The guests fill up the form with necessary details and then a qrcode is sent to the guest’s email address that is used as a pass to the meeting. At the time of meeting, the guest scans the qrcode. If the person is allowed then the door will open that is connected to Arduino else there will be a voice that says that “you are not allowed”.

![Overview](/Images/overview.jpeg)

## Working Of SES

### Module-1: SES Website

The process of the giving pass or card to the person that confirms that the person is allowed or not is done with a website developed using **Django Framework**.

The user that has to organize the function has to sign-up here. Once the signup process is done, login can be done.

![Login](/Images/1.jpg)

Once the user logins, the home page shows all the events that he has created. It contains the information like date of the event, max limit of persons allowed, total number of persons, URL of the form that is shared with the guest, etc.The user can either create a new Event or a new meeting.

![Home](/Images/2.jpg)

In the new event, the details like title, date, time, destination etc. are filled. After adding the event a form is generated and its URL is shared to the guests. The guests fill the form and then a qrcode is sent to their email address which acts as a pass to the event.

![New Event](/Images/3.jpg)

![Form](/Images/6.jpg)

In the new meeting, the URL that contains the form is not shared. Instead there is an option to add the Attendees email.
The qrcode is generated and sent to the respective email addresses which acts as a pass to the meeting.

![New Meeting](/Images/4.jpg)

![Email sent with qrcode](/Images/5.jpg)

### Module-2: SES Software

Now the process of checking whether the person is authorized or not is done by a software made in python that uses image processing. For this python-OpenCV is used. The guest’s qrcode is scanned at the entrance. The unique id that is stored in the qrcode is verified in the database. If the id is found then the door is opened by arduino else there is a voice that says that “you are not allowed.”

The PyFirmata module is used to control the arduino using python. The user can download the database from the home page where all the events/meetings are shown. Also this software can be downloaded from the site in downloads section.

