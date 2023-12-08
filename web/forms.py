from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Booking,Contact
from django.forms import widgets


class Booking(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ("timestamp",)
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control input", "placeholder": "Your name"}),
            "phone": forms.TextInput(attrs={"class": "form-control input", "placeholder": "Your Phone"}),
            "service_date": forms.DateInput(attrs={"class": "form-control input", "placeholder": "Service Date", "type":"date"}),
            "service_time": forms.Select(attrs={"class": "select2 select","placeholder": "Service_time",}),
            "services": forms.Select(attrs={"class": "select2 select","placeholder": "Services",}),
            "service_master": forms.Select(attrs={"class": "select2 select","placeholder": "Service Master",}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'subject','email','message']
        widgets = {
            "name": widgets.TextInput(attrs={"class": "form-group", "placeholder": "Please enter your name"}),
            "phone": widgets.TextInput(attrs={"class": "form-group", "placeholder": "Your Phone"}),
            "subject": widgets.TextInput(attrs={"class": "form-group", "placeholder": "Please enter your Subject"}),
            "email": widgets.EmailInput(attrs={"class": "form-group","placeholder": "Your Email Address",}),
            "message": widgets.Textarea(attrs={"class": "form-group","placeholder": "Type Your Message",}),
        }