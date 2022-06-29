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
    rcount, created= RequestCount.objects.get_or_create(host=r.host, method=r.method, version=r.version)
    rcount.counter = rcount.counter + 1
    rcount.save()
    r.save()
    return HttpResponse()


def metrics(request):
    recalculate()
    reqs = RequestCount.objects.all()
    response = ""
    for req in reqs:
        response += "request_count{host=\""+str(req.host)
        response += "\",method=\""+str(req.method)
        response += "\",version=\""+str(req.version)
        response += "\"} "+str(req.counter)+"\n"
    mets = Metrics.objects.all()
    for met in mets:
        response += "max_request_duration_milliseconds{host=\"" + str(met.host)
        response += "\"} "+str(met.maxTime)+"\n"
        response += "min_request_duration_milliseconds{host=\"" + str(met.host)
        response += "\"} "+str(met.minTime)+"\n"
        response += "mean_request_duration_milliseconds{host=\"" + str(met.host)
        response += "\"} "+str(met.meanTime)+"\n"
    return HttpResponse(response)