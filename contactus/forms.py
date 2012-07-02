from django.forms.models import ModelForm
from contactus.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact