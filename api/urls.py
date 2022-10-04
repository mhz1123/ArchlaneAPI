from django.urls import path
from . import views

urlpatterns = [
    path('/', views.getUsr),
    path('postUser/', views.postUsr),
]