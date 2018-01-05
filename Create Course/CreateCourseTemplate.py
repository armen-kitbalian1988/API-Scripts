# -*- coding: utf8 -*-
import requests
import json

#API URL with parameters
BASE_URL = 'PLACEHOLDER_BRIDGE_INSTANCE_URL'
url = BASE_URL + 'PLACEHOLDER_API_URI' #this is the API URI

#API Authorization in base64 format
base64string =  'PLACEHOLDER_API_TOKEN'

#header with authorization to access the Bridge API
bridgeHeaders = {'content-type': 'application/json', 'Authorization': 'Basic ' + str(base64string)}


#payload can only have one user at a time. For multiple users, use a for loop
apiPayload = {'course_templates': [{'title': 'APICreatedCourse', 'Description' : 'This course was created using the API', 'is_published' : 'false', 'has_unpublished_changes' : 'false', 'default_days_until_due' : '7', 'course_type' : 'bridge'}]}

#call where json is the data type sent as the payload. The response is captured in bridgeResponse
bridgeResponse = requests.post(url, json=apiPayload, headers=bridgeHeaders)

#Debugging
print("Request sent: " + url + json.dumps(apiPayload))
print("Bridge Response: " + str(bridgeResponse.text))

#Write Response to file
file = open('CreateCourseResponse.json','w') 
file.write('Status Code: ' + str(bridgeResponse.status_code) + '\nResponse Body ' + str(bridgeResponse.text))
file.close() 