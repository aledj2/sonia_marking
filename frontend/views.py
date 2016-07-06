from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from .models import *
from django.template import RequestContext
import datetime
from .forms import *

def SelectClass(request):
    classes=Classes.objects.all()
    cutoff=datetime.date.today()-datetime.timedelta(days=30)
    expired_students=Students.objects.filter(datemarked__lt=cutoff).all()
    #return render_to_response('frontend/home.html',classes, context_instance=RequestContext(request))
    return render(request,'frontend/home.html',{'classes':classes, 'expiredStudents':expired_students,})
    
    
def AddMarking(request,classid):
    if request.POST:
        form = add_marking_form(request.POST)
        if form.is_valid():
            progressid = form.cleaned_data['idprogress']
            progress7=progress6
            progress6=progress5
            progress5=progress4
            progress4=progress3
            progress3=progress2
            progress2=progress1
            progress1=datemarkedprogress
            datemarkedprogress=progressid
            progress7_date=progress6_date
            progress6_date=progress5_date
            progress5_date=progress4_date
            progress4_date=progress3_date
            progress3_date=progress2_date
            progress2_date=progress1_date
            progress1_date=datemarked
            return HttpResponse(progress7,progress6,progress5,progress4,progress3,progress2,progress1,datemarkedprogress,progress7_date,progress6_date,progress5_date,progress4_date,progress3_date,progress2_date,progress1_date)
            #return HttpResponseRedirect('/home/')
            #return render(request,'frontend/addmarking.html',{'expiredStudents':expired_students,'ok_students':ok_students,'classname':classname, 'cutoff':cutoff,'form':form})
            
    else:
        form=add_marking_form
        
    classid=str(classid)
    cutoff=datetime.date.today()-datetime.timedelta(days=30)
    expired_students=Students.objects.filter(idclass=classid).filter(datemarked__lt=cutoff).all()
    ok_students=Students.objects.filter(idclass=classid).filter(datemarked__gte=cutoff).all()
    classname=Classes.objects.filter(idclasses=classid).first()
    form=add_marking_form
    return render(request,'frontend/addmarking.html',{'expiredStudents':expired_students,'ok_students':ok_students,'classname':classname, 'cutoff':cutoff,'form':form})
        
