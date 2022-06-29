from django.contrib import admin
from django.urls import path
import receiver.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('receive/', receiver.views.receive),
    path('metrics', receiver.views.metrics)
]
