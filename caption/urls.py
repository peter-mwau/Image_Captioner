from django.urls import path, include
from . import views
from .views import image_request

app_name = 'caption'
urlpatterns = [
    # path('', views.Caption, name='index'),
    path('', views.image_request, name = "image-request"),
]


  
