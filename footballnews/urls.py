from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='footballnews-home'),
    path('info',views.info,name='footballnews-information')
]
