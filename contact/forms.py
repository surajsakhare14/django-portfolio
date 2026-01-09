from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """
    Contact form with built-in validation.
    """

    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]

        widgets = {
            "name": forms.TextInput(attrs={"class": "w-full p-2 border rounded"}),
            "email": forms.EmailInput(attrs={"class": "w-full p-2 border rounded"}),
            "subject": forms.TextInput(attrs={"class": "w-full p-2 border rounded"}),
            "message": forms.Textarea(attrs={"class": "w-full p-2 border rounded", "rows": 4}),
        }
