from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def sri(request):
    tn=input('enter topic')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    return HttpResponse('completed')
def nath(request):
    tn=input('enter topic')
    name=input('enter name')
    url=input('enter url')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
    W.save()
    return HttpResponse('completed')
    