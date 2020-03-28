from django.contrib import admin

from appdata.models import CountryModel, StateModel, CityCasesModel
from intro.models import SupportModel

admin.site.register(CountryModel)
admin.site.register(StateModel)
admin.site.register(CityCasesModel)
admin.site.register(SupportModel)
