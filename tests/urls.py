from django import VERSION
from django.conf.urls import include
from django.contrib import admin

if VERSION[0] < 2:
    from django.conf.urls import url
    admin.autodiscover()
    urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
    ]
else:
    from django.urls import path
    urlpatterns = [
        path('admin/', admin.site.urls),
    ]
