from django.db import models
from django.contrib.auth.models import User


class Test(models.Model):
    name       = models.CharField (max_length=100)
    output     = models.TextField (null=True, blank=True)
    expected   = models.TextField (null=True, blank=True)


# class Page(models.Model):
#     url             = models.CharField (unique=True, max_length=200)
#     text            = models.TextField (null=True, blank=True)
#     html            = models.TextField (null=True, blank=True)
#     expected_text   = models.TextField (null=True, blank=True)
#     expected_html   = models.TextField (null=True, blank=True)
