from gumphone import Gumscp
from smsapi import SMS
from sendlist import Sendlist

#### DEPENDENCIES #####
# bs4
# selenium
# openpyxl
##### REQUIRED #####
# phantomJS


# Reformate phone and name to Textmarketer format :
def reformate_phone_and_name(phone, name):
	r_name = (name.lower()).title()
	if(phone[:2] == '07'):
		r_phone = '44'+phone[1:]
	else:
		r_phone = None

	return r_phone, r_name


if __name__ == "__main__":
	# Scrape and send SMS on the run

	# BLACKBETTY CLOTHING

	# SCRAPE LIST
	sc = Gumscp()
	#sendlist = Sendlist() - Bugged, need to be fixed. We're using phone_send_list to replace the sendlist()
	count = 1
	phone_send_list = []
	today_send_list = []
	# ADD GLOBAL LOOP FOR PAGES
	for j in range(6, 50):

		p_list = sc.scrape('https://www.gumtree.com/property-for-sale/uk/page', j)
		phone_list = []
		today_list = []
		# SEND SMS
		for i in range(0, len(p_list['name'])):

			r_phone, r_name = reformate_phone_and_name(p_list['phone'][i], p_list['name'][i])
			

			##phone_send_list = sendlist.load_list()

			if (r_phone is not None and r_phone not in phone_send_list):
				today_list.append(r_name+','+r_phone)	
				print('sending SMS to... '+r_name+' at this number: '+r_phone)

				## Send SMS
				try:
					sms = SMS()
					# Textmarketer API (API ID, API PWD, Phone Number, Name, Sender Name, i)
					#sms.build('YOUR_API_ID', 'YOUR_API_PWD', r_phone, r_name, 'SENDER_NAME', i)
					#sms.send()
					count = count+1
					today_list.append(r_phone)
				except:
					pass

				phone_list.append(r_phone)

				##sendlist.update_list(phone_list)

		#phone_send_list = phone_send_list + phone_list
		today_send_list = today_send_list + today_list
		print(today_send_list)

		print('All SMS send... Scraping next page...')
	print('Over. Number of SMS: '+str(count))
	print('\n\n\n\n\n\n')
	#print(phone_send_list)
	print('today send list:')
	print(today_send_list)