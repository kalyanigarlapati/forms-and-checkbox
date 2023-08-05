from django.shortcuts import render
from django.http import HttpResponse
from app1.models import *

# Create your views here.
def first(request):
         if request.method =='POST':
         
            username=request.POST['un']
            password=request.POST['pw']
            print(username)
            print(password)
            return HttpResponse(' data submitted')
         return render(request,'first.html')




def inserttopic(request):
      if request.method=='POST':
            topic=request.POST['topic']
            TO=Topic.objects.get_or_create(topic_name=topic)[0]
            TO.save()
            return HttpResponse('insertion is done')
                                                            
      return render(request,'inserttopic.html')


def insertwebpage(request):
      LTO=Topic.objects.all()
      d={'LTO':LTO}
      if request.method=='POST':
            tn=request.POST['tn']
            na=request.POST['na']
            ur=request.POST['ur']
            TO=Topic.objects.get(topic_name=tn)
            WO=Webpage.objects.get_or_create(topic_name=TO,name=na,URL=ur)[0]
            WO.save()
            return HttpResponse('webpage created')
      return render(request,'insertwebpage.html')
            
              
def retrieve(request):
      LTO=Topic.objects.all()
      d={'LTO':LTO}
      if request.method=='POST':
            msts=request.POST.getlist('topic')
            print(msts)
            rwos=Webpage.objects.none()
            for i in msts:
                  rwos=rwos|Webpage.objects.filter(topic_name=i)
                  d1={'rwos':rwos}
            
            return HttpResponse('hai')
      return render(request,'retrieve.html',d)
            
def checkbox(request):
      LTO=Topic.objects.all()
      d={'LTO':LTO}
      return render(request,'checkbox.html',d)    
