from django.db import models
from django.utils import timezone

from appdata.helper import unique_slug_generator


class CountryModel(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)
    slug = models.CharField(max_length=70, default="")

    class Meta:
        db_table = 'countries'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(name=self.name, class_name=CountryModel)
        super().save(*args, **kwargs)


class StateCasesModel(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE, related_name='county_of_state')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)
    slug = models.CharField(max_length=70, default="")
    total_cases = models.IntegerField(null=True, blank=True)
    total_deaths = models.IntegerField(null=True, blank=True)
    total_recovers = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'state'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(name=self.name, class_name=StateCasesModel)
        super().save(*args, **kwargs)


class CityCasesModel(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey(StateCasesModel, on_delete=models.CASCADE, related_name='state_of_city')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)
    slug = models.CharField(max_length=70, default="")
    total_cases = models.IntegerField(null=True, blank=True)
    total_deaths = models.IntegerField(null=True, blank=True)
    total_recovers = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'city_cases'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(name=self.name, class_name=CityCasesModel)
        super().save(*args, **kwargs)

#
# class VirusCases(models.Model):
#     pass
