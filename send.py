from gumphone import Gumscp
from smsapi import SMS
from sendlist import Sendlist
from time import sleep

# Reformate phone and name :
def reformate_phone_and_name(phone, name):
	r_name = (name.lower()).title()
	r_phone = phone
	return r_phone, r_name


if __name__ == "__main__":
	# Scrape and send SMS on the run
	print('Starting now...')
	# HONYZE
	count = 1

	phone_list = []
	name_list = []
	#test:
	#phone_list = ['447584778558']
	#name_list = ['Franky']

	p_list = {'phone':phone_list, 'name':name_list}
	# ADD GLOBAL LOOP FOR PAGES
	for i in range(0, len(p_list['phone'])):

		r_phone, r_name = reformate_phone_and_name(p_list['phone'][i], p_list['name'][i])	
		if (r_phone is not None):

			print('sending SMS to... '+r_name+' at this number: '+r_phone)

			## Send SMS
			try:
				sms = SMS()
				sms.build('YOUR_API_KEY', 'YOUR_API_PWD', r_phone, r_name, 'YOUR_NAME', i)
				sms.send()
				print('SMS has been sent to '+str(r_name)+':'+str(r_phone))

				#print('Pausing for 30s...')
				#sleep(20)
				count = count+1
				#today_list.append(r_phone)
			except:
				pass

	print('Over. Number of SMS: '+str(count))
