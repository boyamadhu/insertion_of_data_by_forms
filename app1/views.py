from django.shortcuts import render
from app1.models import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['topic']
        TO=topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('submitted successfully')
    return render(request,'first.html')

def insert_webpage(request):
    WO=topic.objects.all()
    d={'webpage':WO}
    if request.method=='POST':
        tn=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        TO=topic.objects.get(topic_name=tn)
        WO=webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WO.save()
        return HttpResponse('submitted successfully')
    return render(request,'insert_webpage.html',d)


def insert_access(request):
    WP=webpage.objects.all()
    d={'webpage':WP}
    if request.method=='POST':
        tn=request.POST['name']
        author=request.POST['author']
        date=request.POST['date']
        TO=webpage.objects.get(name=tn)
        AO=access.objects.get_or_create(name=TO,author=author,date=date)[0]
        AO.save()
        return HttpResponse('submitted successfully')
    return render(request,'insert_access.html',d)

