from django.contrib.auth.models import User
from django import forms


class UserSearchForm(forms.Form):
    search_query = forms.CharField(label='Search for a user')

    def search_users(self):
        search_query = self.cleaned_data.get('search_query')
        users = User.objects.filter(username__icontains=search_query)
        return users

