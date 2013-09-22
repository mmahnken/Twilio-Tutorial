from flask import Flask, request, render_template
from flask import render_template
from app import app
from twilio.util import TwilioCapability
from twilio.rest import TwilioRestClient

@app.route('/')
@app.route('/hello')
def hello():
	return "Hello world!"

@app.route('/client', methods=['GET', 'POST'])
def client():
	"""Respond to incoming requests"""
	account_sid = 'AC324fcac164de8fa3e412a7747c1bb884'
	auth_token = '8018f62a5ce49f4399f5855e9ab53f0f'
	application_sid = "APabe7650f654fc34655fc81ae71caa3ff"
	"""Generate the secure capability token"""
	capability = TwilioCapability(account_sid, auth_token)
	capability.allow_client_outgoing(application_sid)
	token = capability.generate()
	return render_template('client.html', token = token)

@app.route('/smsform', methods=['GET', 'POST'])
def smsform():
	account_sid = 'AC324fcac164de8fa3e412a7747c1bb884'
	auth_token = '8018f62a5ce49f4399f5855e9ab53f0f'
	application_sid = "APabe7650f654fc34655fc81ae71caa3ff"
	return render_template('texting.html')

@app.route('/text', methods =['GET', 'POST'])
def text():
	account_sid = 'AC324fcac164de8fa3e412a7747c1bb884'
	auth_token = '8018f62a5ce49f4399f5855e9ab53f0f'
	application_sid = "APabe7650f654fc34655fc81ae71caa3ff"
	client = TwilioRestClient(account_sid, auth_token)
	message = request.form['message']
	message = client.sms.messages.create(body=message, 
		to="+15202479881",
		from_="+16782939090")
	print message.sid
	return "sms sent"
