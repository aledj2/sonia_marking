from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import Classes, Students, BookMarked
from django.template import RequestContext
import datetime

def SelectClass(request):
    
    classes=Classes.objects.all()
    #return render_to_response('frontend/home.html',classes, context_instance=RequestContext(request))
    return render(request,'frontend/home.html',{'classes':classes})
    
def AddMarking(request,classid):
    classid=str(classid)
    cutoff=datetime.date.today()-datetime.timedelta(days=30)
    expired_students=Students.objects.filter(idclass=classid).filter(datemarked__lt=cutoff).all()
    ok_students=Students.objects.filter(idclass=classid).filter(datemarked__gte=cutoff).all()
    classname=Classes.objects.filter(idclasses=classid).first()    
    
    return render(request,'frontend/addmarking.html',{'expiredStudents':expired_students,'ok_students':ok_students,'classname':classname, 'cutoff':cutoff})
        
