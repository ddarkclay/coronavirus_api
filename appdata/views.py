from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from appdata.models import CountryModel, StateCasesModel, CityCasesModel
from appdata.serializers import CountriesSerializers, StatesSerializers, CitiesSerializers, StateCasesSerializer, \
    CountyCasesSerializer
from coronavirus_api.settings import DOMAIN


class Routes(APIView):
    @staticmethod
    def get(request):
        url_data = {
            'countries': DOMAIN + 'api/countries/',
            'single-country': DOMAIN + 'api/countries/india/',
            'states': DOMAIN + 'api/states/',
            'single-state': DOMAIN + 'api/states/maharashtra/',
            'cities': DOMAIN + 'api/cities/',
            'single-city': DOMAIN + 'api/cites/pune/',
            'country-cases': DOMAIN + 'api/cases/country/',
            'single-country-cases': DOMAIN + 'api/cases/country/india/',
            'states-cases': DOMAIN + 'api/cases/state/',
            'single-state-cases': DOMAIN + 'api/cases/state/maharashtra/'
        }
        return Response(url_data, status=status.HTTP_200_OK)


class CountriesViewSet(APIView):
    @staticmethod
    def post(request):
        coutry_srlzer = CountriesSerializers(request.data)
        try:
            coutry_srlzer.is_valid(raise_exception=True)
            coutry_srlzer.save()
            return Response({'message': 'Country added successfully', 'details': coutry_srlzer.data},
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({'message': 'Something went wrong', 'details': e}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request, country_slug=None):
        if country_slug:
            try:
                country_obj = CountryModel.objects.get(slug=country_slug, is_active=True)
                country_srlzer = CountriesSerializers(country_obj)
                return Response(country_srlzer.data, status=status.HTTP_200_OK)
            except CountryModel.DoesNotExist:
                return Response({'message': 'Country does not exists'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            courtries_obj = CountryModel.objects.filter(is_active=True)
            countries_srlzer = CountriesSerializers(courtries_obj, many=True)
            return Response(countries_srlzer.data, status=status.HTTP_200_OK)

    @staticmethod
    def put(request, country_slug):
        try:
            country_obj = CountryModel.objects.get(slug=country_slug, is_active=True)
            country_srlzer = CountriesSerializers(request.data, country_obj)
            return Response({'message': 'Country updated successfully', 'details': country_srlzer.data},
                            status=status.HTTP_200_OK)
        except CountryModel.DoesNotExist:
            return Response({'message': 'Country does not exists'}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, country_slug):
        try:
            country_obj = CountryModel.objects.get(slug=country_slug, is_active=True)
            country_obj.is_active = False
            return Response({'message': 'Country delete successfully'}, status=status.HTTP_200_OK)
        except CountryModel.DoesNotExist:
            return Response({'message': 'Country does not exists'}, status=status.HTTP_400_BAD_REQUEST)


class StatesViewSet(APIView):
    @staticmethod
    def post(request):
        state_srlzer = StatesSerializers(request.data)
        try:
            state_srlzer.is_valid(raise_exception=True)
            state_srlzer.save()
            return Response({'message': 'State added successfully', 'details': state_srlzer.data},
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({'message': 'Something went wrong', 'details': e}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request, state_slug=None):
        if state_slug:
            try:
                state_obj = StateCasesModel.objects.get(slug=state_slug, is_active=True)
                state_srlzer = StatesSerializers(state_obj)
                return Response(state_srlzer.data, status=status.HTTP_200_OK)
            except StateCasesModel.DoesNotExist:
                return Response({'message': 'State does not exists'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            states_obj = StateCasesModel.objects.filter(is_active=True)
            states_srlzer = StatesSerializers(states_obj, many=True)
            return Response(states_srlzer.data, status=status.HTTP_200_OK)

    @staticmethod
    def put(request, state_slug):
        try:
            state_obj = StateCasesModel.get(slug=state_slug, is_active=True)
            state_srlzer = StatesSerializers(request.data, state_obj)
            return Response({'message': 'State updated successfully', 'details': state_srlzer.data},
                            status=status.HTTP_200_OK)
        except StateCasesModel.DoesNotExist:
            return Response({'message': 'State does not exists'}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, state_slug):
        try:
            state_obj = StateCasesModel.objects.get(slug=state_slug, is_active=True)
            state_obj.is_active = False
            return Response({'message': 'State delete successfully'}, status=status.HTTP_200_OK)
        except StateCasesModel.DoesNotExist:
            return Response({'message': 'State does not exists'}, status=status.HTTP_400_BAD_REQUEST)


class CitiesViewSet(APIView):
    @staticmethod
    def post(request):
        city_srlzer = CitiesSerializers(request.data)
        try:
            city_srlzer.is_valid(raise_exception=True)
            city_srlzer.save()
            return Response({'message': 'City added successfully', 'details': city_srlzer.data},
                            status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({'message': 'Something went wrong', 'details': e}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request, city_slug=None):
        if city_slug:
            try:
                city_obj = CityCasesModel.objects.get(slug=city_slug, is_active=True)
                city_srlzer = CitiesSerializers(city_obj)
                return Response(city_srlzer.data, status=status.HTTP_200_OK)
            except CityCasesModel.DoesNotExist:
                return Response({'message': 'City does not exists'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            city_obj = CityCasesModel.objects.filter(is_active=True)
            city_srlzer = CitiesSerializers(city_obj, many=True)
            return Response(city_srlzer.data, status=status.HTTP_200_OK)

    @staticmethod
    def put(request, city_slug):
        try:
            city_obj = CityCasesModel.get(slug=city_slug, is_active=True)
            city_srlzer = CitiesSerializers(request.data, city_obj)
            return Response({'message': 'City updated successfully', 'details': city_srlzer.data},
                            status=status.HTTP_200_OK)
        except CityCasesModel.DoesNotExist:
            return Response({'message': 'City does not exists'}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, city_slug):
        try:
            city_obj = CityCasesModel.objects.get(slug=city_slug, is_active=True)
            city_obj.is_active = False
            return Response({'message': 'City delete successfully'}, status=status.HTTP_200_OK)
        except CityCasesModel.DoesNotExist:
            return Response({'message': 'City does not exists'}, status=status.HTTP_400_BAD_REQUEST)


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
                state_obj = StateCasesModel.objects.get(slug=state_slug, is_active=True)
                state_case_srlzer = StateCasesSerializer(state_obj)
            except StateCasesModel.DoesNotExist:
                return Response({'message': 'State does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            states_obj = StateCasesModel.objects.filter(is_active=True)
            state_case_srlzer = StateCasesSerializer(states_obj, many=True)
        return Response(state_case_srlzer.data, status=status.HTTP_200_OK)
