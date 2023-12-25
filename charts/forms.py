from django import forms

CHART_CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart'),
)
class chartsForm(forms.Form):
    
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)
