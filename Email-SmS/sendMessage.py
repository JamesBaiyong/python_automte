from twilio.rest import Client

accountSID='youraccounSID'
authToken='yourauthToken'
myNumber='+8618888888888'
twilioNumber='+15555555555'

def textmyself(message):
	twilioCli = Client(accountSID,authToken)
	twilioCli.api.account.messages.create(body=message,from_=twilioNumber,to=myNumber)
