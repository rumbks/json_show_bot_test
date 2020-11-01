from django.db import models


class User(models.Model):
    id = models.IntegerField(null=False, primary_key=True, blank=False, unique=True)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=True)
    language_code = models.CharField(max_length=2, null=True)
