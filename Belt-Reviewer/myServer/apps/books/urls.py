from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', home, name = "home"),
    url(r'^add_book$', add_book, name="add_book"),
    url(r'^create_review/(?P<id>\d+)$', create_review, name="create_review"),
    url(r'^show/(?P<id>\d+)$', show, name="show"),
    url(r'^user/(?P<id>\d+)$', user, name="user"),
    url(r'^delete/(?P<id>\d+)$', destroy, name="destroy")

]
