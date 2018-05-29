# gumtree-to-sms

## DISCLAIMER / WARNING !

This repository/project is intended for Educational Purposes ONLY. It is not intended to be used for any purpose other than learning, so please do not use it for any other reason than to learn about DOM scraping.

## Introduction ##
-------------

A Python & Selenium script to scrape Gumtree searches for phone number and name, and send customized SMS via Textmarketer.co.uk cheap API.


#### Requirements ####
-------------

python3.6
selenium
bs4
textmarketer.co.uk API keys


## Gumtree To SMS ##
-------------

Replace:

- path_to_chromium
- path_to_phantom_js
- YOUR_API_KEY
- YOUR_API_PWD
- YOUR_NAME

Note: Was used to get property ads. You might want to change the query.

Note: It's a bit messy, it doesn't all work together. I need to fix the link between the scraper and the SMS API.

### gumphone.py ###
-------------

Using Selenium:
- Iterate through each page of the search query and scrape all the ads
- Crawl to each individual ads, reveal and scrape the phone number and name

### smsapi.py ###
-------------

Using Textmarketer API:
- Send personalized SMS using the name

### send.py and main.py ###
-------------

These need to be fixed. 
Working: - send.py -> input name_list and phone_list scraped from gumphone.py and run to send SMSs.



