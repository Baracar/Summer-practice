import time
import requests

def MetaDataCollect(get_response):
    def middleware(request):
        data = {}
        data['method'] = request.method
        t1 = time.time()
        response = get_response(request)
        t2 = time.time()
        data['time'] = (t2 - t1) * 1000
        data['host'] = '127.0.0.1:7000'
        data['version'] = '0.1.2'
        requests.post(url = 'http://127.0.0.1:8000/receive/', data = data)
        return response
    return middleware