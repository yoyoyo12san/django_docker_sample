from django.urls import path
from . import views

app_name = 'templateApp'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('home/<f_name>/<l_name>', views.home, name = 'home'),
    # path('mypage', views.mypage, name='mypage'),
    path('sample1', views.sample1, name='sample1'),
    path('sample2', views.sample2, name='sample2'),
    path('sample', views.sample, name='sample'),
    path('sample3', views.sample3, name='sample3'),
]