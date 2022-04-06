from django.urls import path

from medic import views

urlpatterns =[
    path('',views.landing,name='landing'),
    path('create/',views.createWebString,name='respond with choosen website'),
    path('create/',views.createWebString,name='respond with the form'),
    path('create/webfying/',views.create,name='create html content'),
    path('urls/<str:cName>/',views.webSites,name='show different websites'),
]