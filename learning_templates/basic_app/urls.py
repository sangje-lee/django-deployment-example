from django.conf.urls import url
from . import views
# = from basic_app import views
# Instructor teacher style

# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^others/$', views.other, name='other'),
]
