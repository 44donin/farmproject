from django.urls import path
from . import views
urlpatterns = [
    path('<str:district>/<str:crop>/',views.GetInformation,name='information')
]
