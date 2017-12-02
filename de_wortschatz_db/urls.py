from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^Wortschatz/', include('Wortschatz.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^explorer/', include('explorer.urls')),
]
