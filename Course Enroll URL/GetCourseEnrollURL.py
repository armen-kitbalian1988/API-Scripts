# -*- coding: utf8 -*-
import requests
import json

#API URL 
BASE_URL = 'https://akitbalian.bridgeapp.com'
base64string =  'M2YwNzU5ZjctYzExOS00MjMyLWI1YjItMzUyZWQwMDcyNzA0OjNiMjA0OGZjLWYzMWEtNDVlZS04ZGVlLTZiMzJkNTMwMTRlZQ=='
url = BASE_URL + '/api/author/course_templates/'

#header with authorization to access the Bridge API
bridgeHeaders = {'content-type': 'application/json', 'Authorization': 'Basic ' + str(base64string)}

#Add parameter to URL
url = url + str(150)
 
#call with response
bridgeResponse = requests.get(url, headers=bridgeHeaders)
output = bridgeResponse.json()

enrollURLText = output['course_templates'][0]['enroll_url']

file = open('EnrollURL.json','w') 
file.write('Status Code: ' + str(bridgeResponse.status_code) + '\nResponse Body ' + str(bridgeResponse.text))
file.close() 

#this writes everything from json
#json.dump(output, file)

file.close() 