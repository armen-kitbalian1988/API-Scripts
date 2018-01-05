# -*- coding: utf8 -*-
import requests
import json

#API URL 
BASE_URL = 'BRIDGE_INSTANCE'
base64string =  'API_TOKEN'
url = BASE_URL + 'API_URI'

#header with authorization to access the Bridge API
bridgeHeaders = {'content-type': 'application/json', 'Authorization': 'Basic ' + str(base64string)}

#Add parameter to URL
url = url + str(COURSE_ID)
 
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