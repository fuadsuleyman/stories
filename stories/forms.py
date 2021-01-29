from django import forms
from stories.models import Contact

class ContactForm(forms.ModelForm):
    # name = forms.CharField(label='Name')
    # email = forms.EmailField(label='Email')
    # subject = forms.CharField(label='Subject')
    # message = forms.CharField(label='Message')

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'content']