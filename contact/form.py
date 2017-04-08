from django import forms
from django.core.validators import validate_email
from captcha.fields import ReCaptchaField


class SendMailForm(forms.Form):
    re_captcha = ReCaptchaField(
        attrs={'lang': 'ro'}
    )
    sender_name = forms.CharField(label="Name", widget=forms.TextInput(attrs={}), required=True)
    sender_email = forms.CharField(label="Email", widget=forms.EmailInput(attrs={}), required=True)
    sender_text = forms.CharField(widget=forms.Textarea(), required=True)

    def __init__(self, *args, **kwargs):
        super(SendMailForm, self).__init__(*args, **kwargs)

    def clean_sender_email(self):
        email = self.cleaned_data.get('sender_email')
        if validate_email(email):
            raise forms.ValidationError("Introduceti un email valid!")
        return email