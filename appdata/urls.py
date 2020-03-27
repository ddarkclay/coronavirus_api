from django.urls import path

from appdata.views import StatesCasesView, CountryCasesView

urlpatterns = [
    path('country/<str:country_slug>/', CountryCasesView.as_view()),
    path('country/', CountryCasesView.as_view()),
    path('state/<str:state_slug>/', StatesCasesView.as_view()),
    path('state/', StatesCasesView.as_view()),
]
