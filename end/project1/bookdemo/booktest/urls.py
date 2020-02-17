# 引入路由绑定函数
from django.conf.urls import url
from . import views
app_name = 'booktest'

urlpatterns = [
    # '^s'  以空格开头  以空格结尾 进入首页
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^delete/(\d+)/$', views.delete, name='delete'),
    url(r'^deletehero/(\d+)/$', views.deletehero, name='deletehero'),
    url(r'^addhero/(\d+)/$', views.addhero, name='addhero'),
    # url(r'^edithero/(\d+)/$', views.edithero, name='edithero')



]