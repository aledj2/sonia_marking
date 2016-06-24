from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import Classes, Students, BookMarked
from django.template import RequestContext

def SelectClass(request):
    
    classes=Classes.objects.all()
    #return render_to_response('frontend/home.html',classes, context_instance=RequestContext(request))
    return render(request,'frontend/home.html',{'classes':classes})
    
    
