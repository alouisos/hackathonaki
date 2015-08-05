import urllib2
from twilio.rest import TwilioRestClient 
import sys
sys.setrecursionlimit(1000000)

url = 'http://techcrunch.com/events/disrupt-sf-hackathon-2015/tickets/'

def get_redirected_url(url):
	import sched, time
	from datetime import datetime
	s = sched.scheduler(time.time, time.sleep)
	# put your own credentials here 
	ACCOUNT_SID = "your_accounts_sid" 
	AUTH_TOKEN = "your_account_token" 
 	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
 	opener = urllib2.build_opener(urllib2.HTTPRedirectHandler)
 	request = opener.open(url)
 	if datetime.now().hour % 12 == 0 and  datetime.now().minute % 60 < 10: # sends message between 12 - 12:10 every day 
 		client.messages.create(
		to="your phone number starting with +", 
		from_="+you need to buy a line here from twilio", 
		body="I am still running baby...", 
		) 		
 		print('it is time to send a message to my father')
	else:
		print('looking forward to sending a message to my father') 
		pass
 	if request.url =="http://techcrunch.com/events/disrupt-sf-hackathon-2015/tickets/":
 		print ('Tickets are open') 
 		client.messages.create(
		to="your phone number starting with +", 
		from_="you need to buy a line here from twilio", 
		body="Hackathon tickets url is open ", 
		)
 		client.messages.create(
		to="your phone number starting with +", 
		from_="you need to buy a line here from twilio", 
		body="Hackathon tickets url is open ", 
		)
		call = client.calls.create(
		to="your phone number starting with +", 
		from_="+you need to buy a line here from twilio", 
		url="https://s3-us-west-1.amazonaws.com/nanotechgalaxy.com/hackathon.xml",  
		method="GET",  
		fallback_method="GET",  
		status_callback_method="GET",  
		if_machine="Continue",  
		record="false"
		) 
		call = client.calls.create(
		to="your phone number starting with +", 
		from_="+you need to buy a line here from twilio", 
		url="url_of_a_server_or_S3_endpoint/hackathon.xml",  # this is the file of what the voice will tell you
		method="GET",  
		fallback_method="GET",  
		status_callback_method="GET",  
		if_machine="Continue",  
		record="false"
		)
 

 		print call.sid
		raise SystemExit(0)
	else:
		print datetime.now()
		print('NO TICKETS YET\n\n')
	s.enter(200, 1, get_redirected_url, (url,))



def initiate_process(): 
	import sched, time
	s = sched.scheduler(time.time, time.sleep)
	s.enter(200, 1, get_redirected_url, (url,))
	s.enter(200, 1, initiate_process, ())
	s.run()
