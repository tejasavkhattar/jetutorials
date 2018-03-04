from django import forms
from .models import contact

class ContactForm(forms.ModelForm):
	class Meta:
		model = contact
		fields = ["email"]

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if not ".com" in email:
			raise forms.ValidationError("Use a Valid Email Address")
		return email


