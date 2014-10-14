from django.conf.urls import patterns, url, include
from .views import flag

urlpatterns = patterns(
    "flags.urls",
    url(r'^flag/$', flag, name="flag"),
)
