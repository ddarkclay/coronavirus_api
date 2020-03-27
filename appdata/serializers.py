from django.db.models import Sum
from rest_framework import serializers

from appdata.models import CountryModel, StateModel, CityCasesModel


class CountriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = CountryModel
        fields = ['name']

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'is_active': instance.is_active,
            'created_at': instance.created_at,
            'updated_at': instance.updated_at,
            'slug': instance.slug,
        }


class StatesSerializers(serializers.ModelSerializer):
    class Meta:
        model = StateModel
        fields = ['name', 'country']

    def get_country(self, instance):
        try:
            country_obj = CountryModel.objects.get(id=instance.country.id, is_active=True)
            country_srlzer = CountriesSerializers(country_obj)
            return country_srlzer.data
        except CountryModel.DoesNotExist:
            return None

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'country': self.get_country(instance),
            'is_active': instance.is_active,
            'created_at': instance.created_at,
            'updated_at': instance.updated_at,
            'slug': instance.slug,
        }


class CitiesSerializers(serializers.ModelSerializer):
    class Meta:
        model = CityCasesModel
        fields = ['name', 'state', 'total_cases', 'total_deaths', 'total_recovers']

    def get_state(self, instance):
        try:
            state_obj = StateModel.objects.get(id=instance.state.id)
            state_srlzer = StatesSerializers(state_obj)
            return state_srlzer.data
        except StateModel.DoesNotExist:
            return None

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'state': self.get_state(instance),
            'is_active': instance.is_active,
            'created_at': instance.created_at,
            'updated_at': instance.updated_at,
            'slug': instance.slug,
            'total_cases': instance.total_cases,
            'total_deaths': instance.total_deaths,
            'total_recovers': instance.total_recovers
        }


class CountyCasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryModel
        field = '__all__'

    def get_states(self, instance):
        states_obj = StateModel.objects.filter(country=instance.id)
        state_case_srlzer = StateCasesSerializer(states_obj, many=True)
        return state_case_srlzer.data

    def to_representation(self, instance):
        total_cases_count, total_deaths_count, total_recovers_count = 0, 0, 0
        total_state_cases = StateModel.objects.filter(country=instance.id)
        for state in total_state_cases:
            cases = CityCasesModel.objects.filter(state=state.id).aggregate(Sum('total_cases'))['total_cases__sum']
            if cases:
                total_cases_count = total_cases_count + int(cases)
            deaths = CityCasesModel.objects.filter(state=state.id).aggregate(Sum('total_deaths'))['total_deaths__sum']
            if deaths:
                total_deaths_count = total_deaths_count + int(deaths)
            recovers = CityCasesModel.objects.filter(state=state.id).aggregate(
                Sum('total_recovers'))['total_recovers__sum']
            if recovers:
                total_recovers_count = total_recovers_count + int(recovers)

        return {
            'id': instance.id,
            'name': instance.name,
            'total_cases': total_cases_count,
            'total_deaths': total_deaths_count,
            'total_recovers': total_recovers_count,
            'states': self.get_states(instance)
        }


class StateCasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateModel
        field = '__all__'

    def get_cities(self, instance):
        cities_obj = CityCasesModel.objects.filter(state=instance.id).values('id', 'name', 'slug', 'total_cases',
                                                                             'total_deaths', 'total_recovers',
                                                                             'created_at', 'updated_at')
        return cities_obj

    def to_representation(self, instance):
        total_city_cases = CityCasesModel.objects.filter(state=instance.id)
        return {
            'id': instance.id,
            'name': instance.name,
            'total_cases': total_city_cases.aggregate(Sum('total_cases'))['total_cases__sum'],
            'total_deaths': total_city_cases.aggregate(Sum('total_deaths'))['total_deaths__sum'],
            'total_recovers': total_city_cases.aggregate(Sum('total_recovers'))['total_recovers__sum'],
            'cities': self.get_cities(instance)
        }
