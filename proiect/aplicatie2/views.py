from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from aplicatie2.models import Pontaj
import datetime


def newPontaj(request):
    Pontaj.objects.create(user_id=request.user.id, start_date=datetime.datetime.now())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def stopTimesheet(request):
    Pontaj.objects.filter(user_id=request.user.id, end_date=None).update(end_date=datetime.datetime.now())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
