from django.conf.urls import url
from django.contrib import admin
from website_hot import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^detail/(?P<id>\d+)/', views.detail, name='detail'),

]
