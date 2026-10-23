from django.contrib import admin

from core.models import Survey


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Survey._meta.get_fields()]
