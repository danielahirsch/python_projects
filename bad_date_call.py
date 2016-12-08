# A program to set up an automatic phone call that reads a message "saving" a person from a potentially bad date. Example: 
# The user is on a bad date and has set up the call to come in at 6:30pm, 30 minutes after the date has started. The call 
# comes in and says "Hi, it's Sarah... I locked myself out of the house and I need you to meet me with my spare key!". Now 
# the user has an excuse to get out of the date if it's not going well. 

from twilio.rest import TwilioRestClient

account_sid = "ACb73219245c97a6f919ab219b33713c3c"
auth_token = "7499f9617aac7c2ba78c80d5fa85e3b8"
client = TwilioRestClient(account_sid, auth_token)

#TODO: add timer that allows the user to schedule the call for a time during the date
call = client.calls.create(to="+972584722226", #any phone number)
                            from_= "+972526954859", #Valid twilio number
                            url="http://twimlets.com/message?Message%5B0%5D=Hey%20Yardena%20I%20need%20you%20to%20come%20home%2C%20something%20is%20wrong%20can%20you%20come%20great%20see%20you%20soon&")
print(call.sid)
