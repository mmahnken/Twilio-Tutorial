from flask.ext.wtf import Form, TextField, TextAreaField, BooleanField, Required, SelectField, IntegerField, DateTimeField

class NewForm(Form):
	field = TextField('id', primary_key = True)

	

