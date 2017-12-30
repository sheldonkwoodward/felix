from django import forms


class MovieForm(forms.Form):
    title = forms.CharField(max_length=250)
    release_year = forms.IntegerField()
    cut = forms.CharField(max_length=250)
    resolution = forms.CharField(max_length=250)
    length_minutes = forms.IntegerField()
    path = forms.CharField()
