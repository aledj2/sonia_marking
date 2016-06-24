from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response
from django.shortcuts import render, get_object_or_404
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.db.models import Q
from .models import *
from .forms import *
import operator


################### splash pages ############################
def home(request):
    return render_to_response('frontend/home.html')