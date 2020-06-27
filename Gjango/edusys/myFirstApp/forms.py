from django.forms import forms
from .models import Schedule


class ScheduleForm(forms.Form):
    class Meta():
        model = Schedule
        fields = ['DAYS_CHOICES']

