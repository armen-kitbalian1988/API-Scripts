# -*- coding: utf8 -*-
import requests
import json

#NOTE: Change the PLACEHOLDER_* parameters to your own values

#API URL with parameters
BASE_URL = 'PLACEHOLDER_BRIDGE_URL'
url = BASE_URL + '/api/admin/users/' #this is the API URI

#API Authorization in base64 format
base64string =  'PLACEHOLDER_BASE64_AUTHORIZATION_TOKEN'

#header with authorization to access the Bridge API
bridgeHeaders = {'content-type': 'application/json', 'Authorization': 'Basic ' + str(base64string)}


#payload can only have one user at a time. For multiple users, use a for loop
apiPayload = {'users': [{'uid': 'PLACEHOLDER_UID', 'first_name' : 'PLACEHOLDER_FIRST_NAME', 'last_name' : 'PLACEHOLDER_LAST_NAME', 'email' : 'PLACEHOLDER_EMAIL'}]}
 
#call where json is the data type sent as the payload. The response is captured in bridgeResponse
bridgeResponse = requests.post(url, json=apiPayload, headers=bridgeHeaders)

#Debugging
print("Request sent: " + url + json.dumps(apiPayload))
print("Bridge Response: " + str(bridgeResponse.text))

#Write Response to file
file = open('CreateUserResponse.json','w') 
file.write('Status Code: ' + str(bridgeResponse.status_code) + '\nResponse Body ' + str(bridgeResponse.text))
file.close() 