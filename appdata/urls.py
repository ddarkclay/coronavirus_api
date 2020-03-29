from django.urls import path

from appdata.views import StatesCasesView, CountryCasesView, Routes, CountriesViewSet, StatesViewSet, CitiesViewSet

urlpatterns = [
    path('countries/<str:country_slug>/', CountriesViewSet.as_view()),
    path('countries/', CountriesViewSet.as_view()),
    path('states/<str:state_slug>/', StatesViewSet.as_view()),
    path('states/', StatesViewSet.as_view()),
    path('cities/<str:city_slug>/', CitiesViewSet.as_view()),
    path('cities/', CitiesViewSet.as_view()),
    path('cases/country/<str:country_slug>/', CountryCasesView.as_view()),
    path('cases/country/', CountryCasesView.as_view()),
    path('cases/state/<str:state_slug>/', StatesCasesView.as_view()),
    path('cases/state/', StatesCasesView.as_view()),
    path('', Routes.as_view()),
]
