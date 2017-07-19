from django.conf.urls import url
from . import views
app_name = 'ninjagold'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^process_money$', views.process_money, name='process_money'),
]
