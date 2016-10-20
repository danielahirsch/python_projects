from twilio.rest import TwilioRestClient

account_sid = "ACb73219245c97a6f919ab219b33713c3c"
auth_token = "7499f9617aac7c2ba78c80d5fa85e3b8"
client = TwilioRestClient(account_sid, auth_token)

#schedule the call for an hour after the date starts
call = client.calls.create(to="+972584722226", #any phone number)
                            from_= "+972526954859", #Valid twilio number
                            url="http://twimlets.com/message?Message%5B0%5D=Hey%20Yardena%20I%20need%20you%20to%20come%20home%2C%20something%20is%20wrong%20can%20you%20come%20great%20see%20you%20soon&")
print(call.sid)