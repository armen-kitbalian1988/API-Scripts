#!/usr/bin/python

import scriptconfig as cfg
import requests
import base64
import json
import zipfile
import os
import downloadDataDump
import csv
import time
from datetime import date, datetime, timedelta
import smtplib
from email.mime.text import MIMEText

#Setup Variables
fromEmail = cfg.fromEmail
toEmail = cfg.toEmail
subject = cfg.emailSubject

daysHistory = 30

#calling the api to download data dump
downloadDataDump.getDataDump(cfg.dataDumpPath)

#object to hold course data 
class UpdatedCourse:
    courseId = 0
    courseTitle = ''
    usermod_id = 0
    fullNameMod = ''
    uidMod = ''
    emailMod = ''
    created_date = ''
    updated_date = ''

#declaration of list of modified courses to process
courseList = []

#set datetime of now to capture only last 30 days
present = datetime.now()
DD = timedelta(days=cfg.days)


#populate from course_template_versions the updated course into the array
with open('/mnt/python/AuditTrail/DataDump/course_template_versions.csv', 'rb') as csvfile:
    #csvreader = csv.reader(csvfile, delimiter=',', quotechar='"') 
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        #convert string to datetime
        updateDate, tmp = row['updated_at'].split(' ')
        updateDate = datetime.strptime(updateDate, "%Y-%m-%d")
        if(updateDate > (present - DD)):
            if(row['event'] == 'update' and row['whodunnit'] != ''):
                #print(row['item_id'], row['whodunnit'], row['event'], row['created_at'], row['updated_at'])
                newCourseObject = UpdatedCourse()
                newCourseObject.courseId = row['item_id'];

                #handle to not best practice column whodunnit... domainID is not currently needed
                domainId, newCourseObject.usermod_id = row['whodunnit'].split('~')
                #print('usermod_id ', newCourseObject.usermod_id)

                newCourseObject.updated_date = row['updated_at']

                #add to list
                courseList.append(newCourseObject)

#Now populate course information, e.g. title 
with open('/mnt/python/AuditTrail/DataDump/course_templates.csv', 'rb') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        for course in courseList:
            if(row['id'] == course.courseId):
                course.courseTitle = row['title']
                course.created_date = row['created_at']

#finally populate the user info of the user who modified the course
with open('/mnt/python/AuditTrail/DataDump/users.csv', 'rb') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        for course in courseList:
            if(row['id'] == course.usermod_id):
                course.fullNameMod = row['full_name']
                course.uidMod = row['uid']
                course.emailMod = row['email']


#now that we have the correct information in memory - write the email body
file = open('emailbody.txt', 'w')
file.write('Please find below the list of courses that have been modified in the last ' + str(daysHistory) + ' days \n\n\n')

for course in courseList:
    file.write('Course: "' + course.courseTitle + '" created at "' + course.created_date + '" has been modified at: "' + course.updated_date + '" by: "' + course.fullNameMod + '" with username: "' + course.uidMod + '" and email: "' + course.emailMod + '"\n' )

    #print(course.courseId, course.courseTitle, course.fullNameMod, course.uidMod, course.emailMod, course.created_date, course.updated_date)
#print('Lenght',  len(courseList)) 
file.close()

#create email message
file = open('emailbody.txt', 'rb')
msg = MIMEText(file.read())
msg['Subject'] = subject
msg['From'] = fromEmail
msg['To'] = toEmail
file.close()

#send out emails
try:
    s = smtplib.SMTP('localhost')
    s.sendmail(fromEmail, [toEmail], msg.as_string())
    s.quit()
except smtplib.SMTPException:
    print('Error')
                          