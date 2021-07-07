from django.urls import path
from . import views
urlpatterns = [
    path('<str:district>/<str:crop>/<str:language>',views.GetInformation,name='information'),
    path('getinfo/',views.GetData,name='getdata')
]
