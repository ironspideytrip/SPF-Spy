#This code is stolen from the official github site of sendgrid
import os
import sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class SendFakeMail:
	def __init__(self,from_email,to_email,api):
		self.from_email=from_email
		self.to_email=to_email
		self.api=api
	def sendfakemessage(self):

		message = Mail(
		    from_email=self.from_email,
		    to_emails=self.to_email,
		    subject='tender',
		    html_content='hello')
		try:
		    sg = SendGridAPIClient(self.api)
		    response = sg.send(message)
		    if response.status_code==202:
			print("[+] Email was sent, now checking whether landed in inbox or not")
		except Exception as e:
		    print("something was interrupted")

