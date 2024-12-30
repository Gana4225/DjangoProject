from django.contrib import admin
from .import models

admin.site.register(models.student)
admin.site.register(models.reg)
admin.site.register(models.branch)
admin.site.register(models.Login)

