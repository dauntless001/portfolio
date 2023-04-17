from django.urls import path
from base import views

app_name = 'base'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about-me/', views.AboutMe.as_view(), name='about'),
    path('talk-to-me/', views.ContactMe.as_view(), name='contact'),
]