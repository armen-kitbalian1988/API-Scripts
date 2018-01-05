# -*- coding: utf8 -*-
import requests
import json

#API URL with parameters
BASE_URL = 'https://akitbalian.bridgeapp.com'
url = BASE_URL + '/api/admin/users/' #this is the API URI

#API Authorization in base64 format
base64string =  'M2YwNzU5ZjctYzExOS00MjMyLWI1YjItMzUyZWQwMDcyNzA0OjNiMjA0OGZjLWYzMWEtNDVlZS04ZGVlLTZiMzJkNTMwMTRlZQ=='

#header with authorization to access the Bridge API
bridgeHeaders = {'content-type': 'application/json', 'Authorization': 'Basic ' + str(base64string)}


#payload can only have one user at a time. For multiple users, use a for loop
apiPayload = {'users': [{'uid': 'test@test.com', 'first_name' : 'testuserFN', 'last_name' : 'testuserLN', 'email' : 'test@test.com'}]}

#call where json is the data type sent as the payload. The response is captured in bridgeResponse
bridgeResponse = requests.post(url, json=apiPayload, headers=bridgeHeaders)

#Debugging
print("Request sent: " + url + json.dumps(apiPayload))
print("Bridge Response: " + str(bridgeResponse.text))

#Write Response to file
file = open('CreateUserResponse.json','w') 
file.write('Status Code: ' + str(bridgeResponse.status_code) + '\nResponse Body ' + str(bridgeResponse.text))
file.close() 