#!/usr/bin/python

import requests
import base64
import json
import time
import datetime
import zipfile
import os

#API_KEY = '3f0759f7-c119-4232-b5b2-352ed0072704'; #content
#API_SECRET = '3b2048fc-f31a-45ee-8dee-6b32d53014ee'; #content
BASE_URL = 'https://akitbalian.bridgeapp.com'; #content
base64string = 'M2YwNzU5ZjctYzExOS00MjMyLWI1YjItMzUyZWQwMDcyNzA0OjNiMjA0OGZjLWYzMWEtNDVlZS04ZGVlLTZiMzJkNTMwMTRlZQ=='; #content

directoryPath = '/Users/akitbalian/Desktop/'
        #base64string = base64.encodestring('%s:%s' % (API_KEY, API_SECRET)).replace('\n', '')
bridgeHeaders = {'content-type': 'application/json', 'Authorization': 'Basic ' + str(base64string)};
url = BASE_URL + '/api/admin/data_dumps/';
url = BASE_URL + '/api/admin/data_dumps/download/';
bridgeResponse = requests.get(url, headers=bridgeHeaders);
print bridgeResponse.text
print bridgeHeaders
with open(directoryPath + "DataDump.zip", "wb") as dDump:
	dDump.write(bridgeResponse.content)
try:
    os.chmod("DataDump.zip", 0o755)
    print "Unzipping..."
    zip_ref = zipfile.ZipFile(directoryPath + "DataDump.zip", 'r')
    zip_ref.extractall(directoryPath + "DataDump/")
    zip_ref.close()
except Exception, e:
    print "Failed to extract" + str(e)

                                                                                           