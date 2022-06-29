from .models import *
from django.db.models import Max, Min
import datetime


def recalculate():
    datetimeShift = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=1)
    reqs = Request.objects.filter(timeStamp__lte=datetimeShift)
    for req in reqs:
        m = Metrics.objects.get(host=req.host)
        if m.minTime == req.time:
            if m.counter > 1:
                m.minTime = Request.objects.filter(host=req.host).order_by('time')[1].time
            else:
                m.minTime = 0
        if m.maxTime == req.time:
            if m.counter > 1:
                m.maxTime = Request.objects.filter(host=req.host).order_by('-time')[1].time
            else:
                m.maxTime = 0
        if m.counter > 1:
            m.meanTime = (m.meanTime * m.counter - req.time)/(m.counter - 1)
        else:
            m.meanTime = 0
        m.counter = m.counter - 1
        m.save()

        rcount = RequestCount.objects.get(host=req.host)
        rcount.counter = rcount.counter - 1
        rcount.save()

        req.delete()
    return
