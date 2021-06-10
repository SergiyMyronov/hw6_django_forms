from django import forms


class LegsForm(forms.Form):
    leg_a = forms.IntegerField(min_value=1)
    leg_b = forms.IntegerField(min_value=1)
