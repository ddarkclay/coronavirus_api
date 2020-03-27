from django.contrib import admin

from appdata.models import CountryModel, StateModel, CityCasesModel

admin.site.register(CountryModel)
admin.site.register(StateModel)
admin.site.register(CityCasesModel)
