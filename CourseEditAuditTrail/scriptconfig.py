#!/usr/bin/python

#Path you'd like the datadump to happen in
dataDumpPath = '/mnt/python/AuditTrail/'

#API & Sandbox Configurations - set these using your Bridge sandbox API token
sandboxURL = 'https://akitbalian.bridgeapp.com'
base64string = 'M2YwNzU5ZjctYzExOS00MjMyLWI1YjItMzUyZWQwMDcyNzA0OjNiMjA0OGZjLWYzMWEtNDVlZS04ZGVlLTZiMzJkNTMwMTRlZQ=='


#Email configurations
toEmail = 'akitbalian@instructure.com'
fromEmail = 'notifications@akitbalian.bridgeapp.com'
emailSubject = 'Course Change Monthly Report'

#Sets the lenth of time to audit in days
days = 30