from tkinter import *
from tkinter import ttk
from twilio.rest import TwilioRestClient

def send():
	account_sid = "ACfda93df2b6adaa2c41cbcb71014688dd"
	auth_token = "269c7339b4cfb88a24f33aaacb708e78"
	client = TwilioRestClient(account_sid, auth_token)
	message = client.sms.messages.create(
		body=text,
		to=receiver,
		from_="+13376602666")
	print (message.sid)
	

receiver = input("Receiver's Number: ")
text = input("Message: ")
go = input("Press the S key to send message: ")

if go == "S":
	send()

if go == "s":
	send()
