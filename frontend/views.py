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
    return render(request,'frontend/home.html',{'classes':classes,'csrf':request, 'expiredStudents':expired_students,})
    
    
def AddMarking(request,classid):
    if request.POST:
        form = add_marking_form(request.POST)
        if form.is_valid():
            progress_id=form.cleaned_data['Add_progress']
            form.save()
            #return HttpResponseRedirect('/register_success/')
            return HttpResponseRedirect('/home/'+str(progress_id))
            ####################################################################
            # progress7=progress6
            # progress6=progress5
            # progress5=progress4
            # progress4=progress3
            # progress3=progress2
            # progress2=progress1
            # progress1=datemarkedprogress
            # datemarkedprogress=progressid
            # progress7_date=progress6_date
            # progress6_date=progress5_date
            # progress5_date=progress4_date
            # progress4_date=progress3_date
            # progress3_date=progress2_date
            # progress2_date=progress1_date
            # progress1_date=datemarked
            ####################################################################
        else:
            return HttpResponseRedirect('/FORMNOTVALID/')
            print form.errors

    else:    
        classid=str(classid)
        cutoff=datetime.date.today()-datetime.timedelta(days=30)
        expired_students=Students.objects.filter(idclass=classid).filter(datemarked__lt=cutoff).all()
        ok_students=Students.objects.filter(idclass=classid).filter(datemarked__gte=cutoff).all()
        classname=Classes.objects.filter(idclasses=classid).first()
        form=add_marking_form
        return render(request,'frontend/addmarking.html',{'csrf':request,'expiredStudents':expired_students,'ok_students':ok_students,'classname':classname, 'cutoff':cutoff,'form':form})

def Markbook(request,studentid):
    if request.POST:
        returned = add_marking_form(request.POST)
        if returned.is_valid():
            #marking = returned.save(commit=False)
            progress_id=returned.cleaned_data['Add_progress']
            if Students.objects.filter(idstudent=studentid).exists():
                studentrecord=Students.objects.get(idstudent=studentid)
                studentrecord.progress7=studentrecord.progress6
                studentrecord.progress6=studentrecord.progress5
                studentrecord.progress5=studentrecord.progress4
                studentrecord.progress4=studentrecord.progress3
                studentrecord.progress3=studentrecord.progress2
                studentrecord.progress2=studentrecord.progress1
                studentrecord.progress1=studentrecord.datemarkedprogress
                studentrecord.datemarkedprogress=progress_id
                studentrecord.progress7_date=studentrecord.progress6_date
                studentrecord.progress6_date=studentrecord.progress5_date
                studentrecord.progress5_date=studentrecord.progress4_date
                studentrecord.progress4_date=studentrecord.progress3_date
                studentrecord.progress3_date=studentrecord.progress2_date
                studentrecord.progress2_date=studentrecord.progress1_date
                studentrecord.progress1_date=studentrecord.datemarked
                classid=Students.objects.filter(idstudent=studentid).values_list('idclass', flat=True).get()
                #s=Students(idstudent=studentid,progress7=new_progress7,progress6=new_progress6,progress5=new_progress5,progress4=new_progress4,progress3=new_progress3,progress2=new_progress2,progress=new_progress1,datemarkedprogress=progress_id,progress7_date=new_progress7_date,progress6_date=new_progress6_date,progress5_date=new_progress5_date,progress4_date=new_progress4_date,progress3_date=new_progress3_date,progress2_date=new_progress2_date,progress1_date=new_progress1_date)
                studentrecord.save()
                
                return HttpResponseRedirect('/add_marking/'+str(classid)+'/')
        else:
            print returned.errors
            return HttpResponseRedirect('/formerror/')

    else:
        form=add_marking_form
        studentid=str(studentid)
        student=Students.objects.filter(idstudent=studentid).all()
        return render(request,'frontend/markbook.html',{'csrf':request,'student':student,'form':form})
