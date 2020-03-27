from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from appdata.models import CountryModel, StateModel, CityCasesModel
from appdata.serializers import CountriesSerializers, StatesSerializers, CitiesSerializers, StateCasesSerializer, \
    CountyCasesSerializer


class CountriesViewSet(viewsets.ModelViewSet):
    queryset = CountryModel.objects.all().order_by('-id')
    serializer_class = CountriesSerializers


class StatesViewSet(viewsets.ModelViewSet):
    queryset = StateModel.objects.all().order_by('-id')
    serializer_class = StatesSerializers


class CitiesViewSet(viewsets.ModelViewSet):
    queryset = CityCasesModel.objects.all().order_by('-id')
    serializer_class = CitiesSerializers


class CountryCasesView(APIView):

    @staticmethod
    def get(request, country_slug=None):
        if country_slug:
            try:
                country_obj = CountryModel.objects.get(slug=country_slug, is_active=True)
                country_cases_srlzer = CountyCasesSerializer(country_obj)
                country_data = country_cases_srlzer.data
            except CountryModel.DoesNotExist:
                return Response({'message': 'Country does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            countries_obj = CountryModel.objects.filter(is_active=True)
            country_cases_srlzer = CountyCasesSerializer(countries_obj, many=True)
            total_cases_count = sum(map(lambda x: int(x['total_cases']), country_cases_srlzer.data))
            total_death_count = sum(map(lambda x: int(x['total_deaths']), country_cases_srlzer.data))
            total_recover_count = sum(map(lambda x: int(x['total_recovers']), country_cases_srlzer.data))
            print('total cases in world ', total_cases_count)
            country_data = {
                'name': 'World Wide',
                'total_cases': total_cases_count,
                'total_deaths': total_death_count,
                'total_recover': total_recover_count,
                'countries': country_cases_srlzer.data
            }
        return Response(country_data, status=status.HTTP_200_OK)


class StatesCasesView(APIView):

    @staticmethod
    def get(request, state_slug=None):
        if state_slug:
            try:
                state_obj = StateModel.objects.get(slug=state_slug, is_active=True)
                state_case_srlzer = StateCasesSerializer(state_obj)
            except StateModel.DoesNotExist:
                return Response({'message': 'State does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            states_obj = StateModel.objects.filter(is_active=True)
            state_case_srlzer = StateCasesSerializer(states_obj, many=True)
        return Response(state_case_srlzer.data, status=status.HTTP_200_OK)
