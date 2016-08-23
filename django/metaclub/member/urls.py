from django.conf.urls import url
from member.views import ViewList

urlpatterns = [
    url(r'^list/$', ViewList.as_view(), name='list'),
]
