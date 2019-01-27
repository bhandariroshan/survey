# Create your models here.

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Survey(models.Model):
    survey_number =models.AutoField(primary_key=True)
    html = models.CharField(max_length=200, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    # Meta and Strings:
    class Meta:
        """ Meta data for Language model"""
        verbose_name = _("Survey")
        verbose_name_plural = _("Survey")

    def __str__(self):
        return self.html


class Codes(models.Model):
    survey = models.ForeignKey('Survey', on_delete=models.CASCADE)
    is_used = models.BooleanField(default=False)
    code = models.CharField(max_length=200, unique=True)
    answer = models.CharField(max_length=200, null=True, blank=True)

    # Meta and Strings:
    class Meta:
        """ Meta data for Language model"""
        verbose_name = _("Code")
        verbose_name_plural = _("Codes")

    def __str__(self):
        return self.code
