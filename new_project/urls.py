from django.urls import path
from django.contrib import admin
from . import views
urlpatterns=[
path('index/',views.index, name='index'),
path('login/',views.login,name='login'),
path('home',views.home,name='home'),
path('category/<int:cid>/',views.category,name='category'),
path('download/<int:my_id>/',views.download,name='download'),
]