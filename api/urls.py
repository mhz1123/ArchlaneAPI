from django.urls import path
from . import views

urlpatterns = [
    path('getUsers/', views.getUsr),
    path('postUser/', views.postUsr),
]