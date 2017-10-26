import os
import time
import re
import json
from urllib.request import urlopen, Request
from urllib.parse import urlencode, quote_plus, quote
from urllib.error import HTTPError, URLError
from random import randint
import requests
from xlsxlib import Excel
import string

class SMS():

    def __init__(self):

        return

    def build(self, username, password, to_number, name, originator, variant):

        # Split - test - here
        
        msg = 'Hi '+name+', I just spotted your ad on Gumtree... www.bit.ly/test123'

        message = urlencode({'message': msg})
        
        print(message)

        self.url = "http://api.textmarketer.co.uk/gateway/"+"?username="+username+"&password="+password+"&option=xml"+"&to="+to_number+"&"+message+"&orig="+originator

        return 

    def send(self):

        response = urlopen(self.url)
        string = response.read().decode('utf-8')
        print(string)

        return

    def send_list(self):

        report = Excel()
        report.open_workbook('result')

        for i in range(1, 201):
            name = report.read_cell(i, 1)
            phone = report.read_cell(i, 2)
            # Transform 07 into 447 numbers & Name
            phone = '44'+phone[1:]
            name = string.capwords(name)
            
            self.build('YOUR_API_KEY', 'YOUR_API_PWD', phone, name, 'SENDER_NAME')
            self.send()
            time.sleep(0.1)
            print ('\n')

        report.save_workbook()
        
        return


