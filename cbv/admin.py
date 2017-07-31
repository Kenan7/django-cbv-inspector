from django.contrib import admin

from . import models

admin.site.register(models.Project)
admin.site.register(models.ProjectVersion)
admin.site.register(models.Module)
admin.site.register(models.Klass)
admin.site.register(models.Inheritance)
admin.site.register(models.KlassAttribute)
admin.site.register(models.ModuleAttribute)
admin.site.register(models.Method)
admin.site.register(models.Function)
