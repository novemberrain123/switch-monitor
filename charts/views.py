from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib import messages

from .models import Pingstatus
from urllib import parse
from datetime import datetime
import json
import logging

logger = logging.getLogger("logsomething")
# Create your views here.

def index(request):
    table = Pingstatus.objects.order_by('-switch_label')[:5]
    template = loader.get_template('charts/index.html')
    context = {
        'table': table,
    }
    return HttpResponse(template.render(context, request))

def calcStatus(request):
    data = {'msg':''}
    if request.method == "POST":
        table = Pingstatus.objects.all()
        for i in table:
            if(i.term_1 + i.term_2 + i.term_3 + i.term_4 + i.term_5 == 0):
                item = Pingstatus.objects.filter(
                    switch_label=i.switch_label,
                    ts=i.ts,
                ).update(
                    switch_status=0
                )
            else:                
                item = Pingstatus.objects.filter(
                    switch_label=i.switch_label,
                    ts=i.ts,
                ).update(
                    switch_status=1
                )
        data['msg'] += "Successfully calculated switch status and updated database."
    return JsonResponse(data)

def chart(request):
    min_date = Pingstatus.objects.order_by('ts').first().ts.strftime("%Y-%m-%d")
    max_date = Pingstatus.objects.order_by('-ts').first().ts.strftime("%Y-%m-%d")
    template = loader.get_template('charts/chart.html')
    context = {
        "min_date": min_date,
        "max_date": max_date,
    }
    return HttpResponse(template.render(context, request))

def getData(request):
    if request.method == "GET":
        data = parse.parse_qsl(request.GET.get("data", None))
        datePart = data[0][1].split("-")
        datePart = [int(x) for x in datePart]
        if data[1][1] == "12":
            fromDate = datetime(datePart[0], datePart[1], datePart[2])
            toDate = datetime(datePart[0], datePart[1], datePart[2], hour=11, minute=59)
        else:
            fromDate = datetime(datePart[0], datePart[1], datePart[2], hour=12)
            toDate = datetime(datePart[0], datePart[1], datePart[2], hour=23, minute=59)

        switches = Pingstatus.objects.order_by().values("switch_label").distinct()
        queryData = Pingstatus.objects.filter(ts__gte=fromDate, ts__lte=toDate)
        data = {}
        for x in switches:
            data["label" + x["switch_label"]] = [x.strftime("%H:%M") for x in queryData.filter(switch_label=x["switch_label"]).values_list("ts", flat=True)]
            data["data" + x["switch_label"]] = list(queryData.filter(switch_label=x["switch_label"]).values_list("switch_status", flat=True))

    return JsonResponse(data)

def alert(request):
    template = loader.get_template('charts/alert.html')
    table = Pingstatus.objects.filter(switch_status=0)
    context = {
        'table': table,
    }
    return HttpResponse(template.render(context, request))



