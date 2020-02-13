# 引入路由绑定函数
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^about/$', views.about),
    url(r'^detail/(\d+)/', views.detail)
]