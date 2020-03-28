from django.urls import path

from intro.views import intro

urlpatterns = [
    path('', intro, name='Intro_Home_Page'),
]