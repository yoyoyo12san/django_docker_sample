from django.urls import path
from . import views

app_name = 'firstapp'

urlpatterns = [
    path('hello', views.index, name='index'),
    path('page/<str:user_name>', views.user_page, name='user_page'),
    path('num/<int:number>', views.number, name='number'),
]