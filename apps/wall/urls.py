from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^message_wall$', views.messageWall),
    url(r'^comments_all$', views.commentsAll),
    url(r'^logout$', views.logOut),

]
