#!/usr/bin/python

import requests
import base64
import json
import time
import datetime
import zipfile

API_KEY = '3f0759f7-c119-4232-b5b2-352ed0072704'; #content
API_SECRET = '3b2048fc-f31a-45ee-8dee-6b32d53014ee'; #content
BASE_URL = 'https://akitbalian.bridgeapp.com'; #content
TOKEN = 'M2YwNzU5ZjctYzExOS00MjMyLWI1YjItMzUyZWQwMDcyNzA0OjNiMjA0OGZjLWYzMWEtNDVlZS04ZGVlLTZiMzJkNTMwMTRlZQ=='; #content

def getDataDump(directoryPath):
	base64string = base64.encodestring('%s:%s' % (API_KEY, API_SECRET)).replace('\n', '')
	bridgeHeaders = {'content-type': 'application/json', 'Authorization': 'Basic %s' % base64string};
	url = BASE_URL + '/api/admin/data_dumps';
	bridgeResponse = requests.post(url, headers=bridgeHeaders);
	print str(bridgeResponse.status_code) + " - " + str(bridgeResponse.raise_for_status());
	j = json.loads(bridgeResponse.text);
	i = 100
	print "Refreshing Data Dump..."
	while (j['data_dumps'][0]['status']=='pending'):
		print "Waiting..."
		time.sleep(5);
		i-=1
		bridgeResponse = requests.get(url, headers=bridgeHeaders);
		j = json.loads(bridgeResponse.text);
		if(j['data_dumps'][0]['status']=='complete'):
			i==0
			print bridgeResponse.text;
			print "Downloading..."
			url = BASE_URL + '/api/admin/data_dumps/download';
			bridgeResponse = requests.get(url, headers={'Authorization': 'Basic %s' % base64string});
			with open(directoryPath + "DataDump.zip", "wb") as dDump:
				dDump.write(bridgeResponse.content)
			try:
				print "Unzipping..."
				zip_ref = zipfile.ZipFile(directoryPath + "DataDump.zip", 'r')
				zip_ref.extractall(directoryPath + "DataDump/")
				zip_ref.close()
			except:
				print "Failed to extract"
			return directoryPath + "DataDump/"
		if(i<=0): #timeout after 10-ish minutes
			print bridgeResponse.text;
			return "Failed. Took too long"

print ("\n" * 100) #clear screen (hack for windows/osx)
print "This tool will download the Data Dump to a directory that you specify. DON'T FORGET to use the closing backslash!"
getDataDump(raw_input('What directory would you like to save the Data Dump to: '))