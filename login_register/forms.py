from django import forms
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control mb-3'
            self.fields[field].widget.attrs['placeholder'] = field
