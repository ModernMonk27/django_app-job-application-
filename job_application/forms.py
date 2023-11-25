from django import forms


class ApplicationForm(forms.Form):
    name = forms.CharField(max_length=80)
    email = forms.EmailField()
    experience = forms.CharField(max_length=80)
    self_intro = forms.CharField(max_length=80)
    preference = forms.CharField(max_length=80)

