from django.contrib import admin
from .models import *

admin.site.site_header = "Survey Settings Admin"
admin.site.site_title = "Survey App Admin Portal"
admin.site.index_title = "Welcome to Survey App Portal"

admin.site.register(Survey)
admin.site.register(Codes)

from django.contrib.auth.models import Group
from allauth.account.models import EmailAddress
from django.contrib.sites.models import Site

admin.site.unregister(Group)
admin.site.unregister(Site)
admin.site.unregister(EmailAddress)
