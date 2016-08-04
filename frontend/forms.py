from django import forms
from models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import operator
from datetime import date

class add_marking_form(forms.ModelForm):       
    CHOICES=(('1','Limited'),('2','Satisfactory'),('3','Good'),('4','Excellent'))
    Add_progress=forms.ChoiceField(label='Add new mark for ',choices=CHOICES)
    
    class Meta:
        model=Students
        fields=('datemarkedprogress',)