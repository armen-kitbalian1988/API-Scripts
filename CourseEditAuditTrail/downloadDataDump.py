#!/usr/bin/python

import scriptconfig as cfg
import requests
import base64
import json
import time
import datetime
import zipfile
import os

BASE_URL = cfg.sandboxURL
base64string = cfg.base64string

def getDataDump(directoryPath):
        bridgeHeaders = {'content-type': 'application/json', 'X-Direct-Download': 'true', 'Authorization': 'Basic ' + str(base64string)};
        url = BASE_URL + '/api/admin/data_dumps/';
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
                        print "Downloading..."
                        url = BASE_URL + '/api/admin/data_dumps/download/';
                        bridgeHeaders = {'content-type': 'application/json', 'X-Direct-Download': 'true', 'Authorization': 'Basic ' + str(base64string)};
                        #the below calls the API but refuses redirects which would causes an error   
                        bridgeResponse = requests.get(url, headers=bridgeHeaders, allow_redirects=False);
                        #the below catches the redirect URL and downloads it without the auth header to prevent the x-Amz error
                        bridgeResponse = requests.get(bridgeResponse.headers['Location'])
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
                        return directoryPath + "DataDump/"
                if(i<=0): #timeout after 10-ish minutes
                        print bridgeResponse.text;
                        return "Failed. Took too long"
