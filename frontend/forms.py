from django import forms
from models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import operator
from datetime import date

class add_marking_form(forms.Form):
    Add_progress=forms.ChoiceField(label='Add new mark for ',choices=Progress.objects.values_list('idprogress','progress_text'))
    