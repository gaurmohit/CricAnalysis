from django import forms

class player11_form(forms.Form):
    batsman = forms.CharField(label = "batsman",
                                         required = True,)
    
    bowler = forms.CharField(label = "bowler",
                                         required = True,)
    