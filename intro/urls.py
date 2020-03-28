from django.urls import path

from intro.views import intro, payment, handlePayment, contact, graph

urlpatterns = [
    path('', intro, name='Intro_Home_Page'),
    path('graph/', graph, name='Graph_Page'),
    path('contact/', contact, name='Contact_Page'),
    path('payment/', payment, name='Support_Page'),
    path('handler-payment/', handlePayment, name='Handle_Payment'),
]
