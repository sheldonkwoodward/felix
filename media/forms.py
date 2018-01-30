from django import forms


class MovieForm(forms.Form):
    title = forms.CharField(max_length=250)
    release_year = forms.IntegerField()
    cut = forms.CharField(max_length=250)
    resolution = forms.CharField(max_length=250)
    length_minutes = forms.IntegerField()
    path = forms.CharField()


class SeasonForm(forms.Form):
    title = forms.CharField(max_length=250)
    season = forms.IntegerField()
    cut = forms.CharField(max_length=250)
    resolution = forms.CharField(max_length=250)
    path = forms.CharField()


class EpisodeForm(forms.Form):
    title = forms.CharField(max_length=250)
    season = forms.IntegerField()
    episode = forms.IntegerField()
    cut = forms.CharField(max_length=250)
    resolution = forms.CharField(max_length=250)
    path = forms.CharField()
