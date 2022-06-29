from django.shortcuts import render
from django.http import *
from django.views.decorators.csrf import csrf_exempt
from .models import *
import datetime
from .scripts import recalculate


@csrf_exempt
def receive(request):
    r = Request()
    r.host = request.POST.get('host')
    r.method = request.POST.get('method')
    r.time = float(request.POST.get('time'))
    r.version = request.POST.get('version')

    m, created = Metrics.objects.get_or_create(host=r.host)
    if  created:
        m.minTime = r.time
        m.maxTime = r.time
        m.meanTime = r.time
        m.counter = 1
    else:
        if m.minTime > r.time:
            m.minTime = r.time
        if m.maxTime < r.time:
            m.maxTime = r.time
        m.meanTime = (m.meanTime * m.counter + r.time)/(m.counter + 1)
        m.counter = m.counter + 1
    m.save()
    r.metrics = m
    r.save()
    return HttpResponse()


def metrics(request):
    datetimeShift = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(seconds=15)
    reqs = Request.objects.filter(timeStamp__gte=datetimeShift)
    response = ""
    for req in reqs:
        response += "request_duration_milliseconds{host=\""+str(req.host)
        response += "\",method=\""+str(req.method)
        response += "\",version=\""+str(req.version)
        response += "\",timestamp=\""+str(req.timeStamp)
        response += "\"} "+str(req.time)+"\n"
    recalculate()
    mets = Metrics.objects.all()
    for met in mets:
        response += "max_request_duration_milliseconds{host=\"" + str(met.host)
        response += "\"} "+str(met.maxTime)+"\n"
        response += "min_request_duration_milliseconds{host=\"" + str(met.host)
        response += "\"} "+str(met.minTime)+"\n"
        response += "mean_request_duration_milliseconds{host=\"" + str(met.host)
        response += "\"} "+str(met.meanTime)+"\n"
    print(response)
    return HttpResponse(response)