from django.contrib import admin
from .models import *

admin.site.site_header = "Survey Settings Admin"
admin.site.site_title = "Survey App Admin Portal"
admin.site.index_title = "Welcome to Survey App Portal"


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    """ Admin class for Sentup Subject Result."""

    list_display = (
        "survey_number", "__str__",
    )

@admin.register(Codes)
class CodesAdmin(admin.ModelAdmin):
    """ Admin class for Sentup Subject Result."""

    list_display = (
        "code", "is_used", "answer",
    )


from django.contrib.auth.models import Group
from allauth.account.models import EmailAddress
from django.contrib.sites.models import Site

admin.site.unregister(Group)
admin.site.unregister(Site)
admin.site.unregister(EmailAddress)


