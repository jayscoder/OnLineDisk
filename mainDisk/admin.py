from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.FileModel)
admin.site.register(models.TextModel)
