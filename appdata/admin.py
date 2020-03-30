from django.contrib import admin

from appdata.models import CountryModel, StateCasesModel, CityCasesModel
from intro.models import SupportModel

admin.site.register(CountryModel)
admin.site.register(StateCasesModel)
admin.site.register(CityCasesModel)
admin.site.register(SupportModel)
